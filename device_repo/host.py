import logging
import Ice
import yaml
import argparse
from collections import namedtuple
from typing import List

from .device_repo_ice import (DeviceRepo, DeviceType, DeviceStatus, DevicePrx,
                              DeviceEntry, UnknownDeviceException,
                              DeviceOccupiedException)

Device = namedtuple('Device', ['id', 'type', 'rack', 'token'])


class DeviceRepoI(DeviceRepo):
    def __init__(self, bind_address, bind_port, logger):
        self.bind_address = bind_address
        self.bind_port = bind_port
        self.logger = logger
        self.ic = None

        self.devices = {}
        self.device_user_map = {}

        self.shutting_down = False

    def register_client(self, connection: Ice.Connection):
        connection.setCloseCallback(lambda conn: self.client_connection_lost(conn))

    def list_devices(self, current=None) -> List[DeviceEntry]:
        self.register_client(current.con)

        return [DeviceEntry(ent.id, ent.type) for ent in self.devices.values()]

    def get_device_type(self, _id, current=None) -> DeviceType:
        self.register_client(current.con)

        if _id not in self.devices:
            raise UnknownDeviceException

        return self.devices[_id].type

    def check_device_status(self, _id, current=None) -> DeviceStatus:
        self.register_client(current.con)

        if _id not in self.devices:
            raise UnknownDeviceException

        return self.devices[_id].rack.check_status(_id)

    def acquire_device(self, _id, current=None) -> DevicePrx:
        self.register_client(current.con)

        if _id not in self.devices:
            raise UnknownDeviceException

        if _id in self.device_user_map:
            if self.device_user_map[_id] == current.con:
                self.logger.info(f"Client {current.con.toString()} attempts to reacquire"
                                 f" device {_id}.")
            else:
                self.logger.warning(f"Client {current.con.toString()} attempted to "
                                    f"acquire occupied device {_id} of "
                                    "others.")
            raise DeviceOccupiedException

        self.device_user_map[_id] = current.con

        self.logger.info(f"Client {current.con.toString()} acquired device {_id}.")
        return self.devices[_id].rack.get_device_prx(_id)

    def release_device(self, _id, current=None):
        self.register_client(current.con)

        if _id not in self.devices:
            raise UnknownDeviceException

        if _id not in self.device_user_map:
            return

        if self.device_user_map[_id] == current.con:
            self.logger.info(f"Client {current.con.toString()} released occupied device"
                             f" {_id}.")
            self.devices[_id].rack.release_device_prx(_id)
            del self.device_user_map[_id]
        else:
            self.logger.warning(f"Client {current.con.toString()} attempted to "
                                f"release occupied device {_id} of "
                                "others.")
            raise DeviceOccupiedException

    def add_device(self, _id, _type, rack, token, current=None):
        rack = rack.ice_context({'token': token})
        try:
            assert(rack.check_status(_id) == DeviceStatus.Idle)
        except Exception as e:
            self.logger.error("Error when adding device: ")
            self.logger.error(e)
            return False

        self.logger.info(f"Device added: {_id}({_type}) from "
                         f"{rack.ice_getIdentity().name}.")

        self.devices[_id] = Device(_id, _type, rack, token)
        rack.ice_getConnection().setCloseCallback(
            lambda conn: self.device_connection_lost(rack))

    def device_connection_lost(self, rack):
        if not self.shutting_down:
            device_to_remove = []
            for dev_id in self.devices.keys():
                if rack == self.devices[dev_id].rack:
                    device_to_remove.append(self.devices[dev_id])

            for dev in device_to_remove:
                if dev.id in self.device_user_map:
                    del self.device_user_map[dev.id]
                del self.devices[dev.id]
                self.logger.warning(f"Lost connection with device {dev.id}.")

    def client_connection_lost(self, connection):
        self.logger.info(f"Client {connection.toString()} disconnected.")
        dev_to_release = []
        for dev, con in self.device_user_map.items():
            if con == connection:
                dev_to_release.append(dev)

        for dev in dev_to_release:
            self.logger.info(f"Automatically release device {dev}.")
            self.devices[dev].rack.release_device_prx(dev)
            del self.device_user_map[dev]

    def start(self):
        ice_props = Ice.createProperties()

        ice_props.setProperty("Ice.ACM.Close", "4")  # CloseOnIdleForceful
        ice_props.setProperty("Ice.ACM.Heartbeat", "3")  # HeartbeatAlways
        ice_props.setProperty("Ice.ACM.Timeout", "10")

        ice_props.setProperty("Ice.ThreadPool.Client.Size", "1")
        ice_props.setProperty("Ice.ThreadPool.Client.SizeMax", "10")
        ice_props.setProperty("Ice.ThreadPool.Server.Size", "1")
        ice_props.setProperty("Ice.ThreadPool.Server.SizeMax", "10")

        ice_init_data = Ice.InitializationData()
        ice_init_data.properties = ice_props

        with Ice.initialize(ice_init_data) as ic:
            self.ic = ic
            adapter = ic.createObjectAdapterWithEndpoints(
                "DeviceRepoAdapter",
                f"tcp -h {self.bind_address} -p {self.bind_port}")

            adapter.add(self, ic.stringToIdentity("DeviceRepo"))

            adapter.activate()
            endpoint_info = adapter.getEndpoints()[0].getInfo()
            self.bind_address = endpoint_info.host
            self.bind_port = endpoint_info.port

            self.logger.info(f"DeviceRepo started at {self.bind_address}:"
                             f"{self.bind_port}.")

            try:
                ic.waitForShutdown()
            except KeyboardInterrupt:
                self.shutting_down = True


def main(start_immediately=True):
    parser = argparse.ArgumentParser(
        description="The host program of the DeviceRepo.")

    parser.add_argument("-b", "--bind", dest="bind", type=str, default="",
                        help="bind address for the host")
    parser.add_argument("-p", "--port", dest="port", type=int,
                        help="bind port for the host", default=0)
    parser.add_argument("-c", "--config", dest="config", type=str, default="",
                        help="path of the config file")
    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
                "[%(asctime)s %(levelname)s] "
                "%(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    config = None
    if args.config:
        with open(args.config, "r") as f:
            config = yaml.safe_load(f)

    if not args.bind:
        try:
            args.bind = config['network']['bind_address']
        except (TypeError, KeyError):
            args.bind = "0.0.0.0"

    if not args.port:
        try:
            args.port = config['network']['bind_port']
        except (TypeError, KeyError):
            args.port = 0

    device_repo_host = DeviceRepoI(args.bind, args.port, logger)
    if start_immediately:
        device_repo_host.start()

    return device_repo_host
