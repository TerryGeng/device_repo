import logging
import time
from typing import Dict
from collections import namedtuple
from secrets import token_hex

import Ice

from .device_repo_ice import (Device, DevicePrx, DeviceRack, DeviceRackPrx,
                              DeviceRepoPrx, DeviceStatus,
                              InvalidTokenException, DeviceOccupiedException,
                              UnknownDeviceException)


DeviceEntry = namedtuple('DeviceEntry', ['device', 'id', 'type'])


class DeviceRackI(DeviceRack):
    def __init__(self, name, host_address, host_port, logger=None):
        self.logger = logger if logger else logging.getLogger()
        self.name = name
        self.devices: Dict[DeviceEntry] = {}
        self.host_address = host_address
        self.host_port = host_port
        self.bind_address = ""
        self.bind_port = -1
        self.token = ""
        self.rack = None
        self.adapter = None
        self.proxies = {}
        self.started = False
        self.ic = None

    def load_device(self, dev_id, dev_obj: Device):
        assert not self.started, ("Devices can not be loaded after the rack "
                                  "has been started.")

        self.devices[dev_id] = DeviceEntry(
            dev_obj,
            dev_id,
            dev_obj.get_type()
        )

    def _check_token(self, current):
        if not current:
            return True

        if 'token' not in current.ctx or current.ctx['token'] != self.token:
            raise InvalidTokenException
        else:
            return True

    def get_device_prx(self, dev_id, current=None) -> DevicePrx:
        self._check_token(current)

        if dev_id in self.proxies:
            self.logger.warning(f"Attempt to acquire occupied {dev_id}.")
            raise DeviceOccupiedException

        if dev_id not in self.devices:
            raise UnknownDeviceException

        prx = DevicePrx.uncheckedCast(self.adapter.addWithUUID(
            self.devices[dev_id].device
        ))
        self.proxies[dev_id] = prx
        self.logger.info(f"{dev_id} acquired.")

        return prx

    def release_device_prx(self, dev_id, current=None):
        self._check_token(current)

        if dev_id not in self.proxies:
            return

        if dev_id not in self.devices:
            raise UnknownDeviceException

        self.adapter.remove(self.proxies[dev_id].ice_getIdentity())
        del self.proxies[dev_id]

        self.logger.info(f"{dev_id} released.")

    def check_status(self, dev_id, current=None) -> DeviceStatus:
        self._check_token(current)

        if dev_id in self.proxies:
            return DeviceStatus.Occupied
        else:
            if dev_id not in self.devices:
                raise UnknownDeviceException
            return DeviceStatus.Idle

    def _connect_and_register_devices(self):
        self.logger.info("Connecting to DeviceRepo at "
                         f"{self.host_address}:{self.host_port}.")

        prx = self.ic.stringToProxy(
            f"DeviceRepo:tcp -h {self.host_address} "
            f"-p {self.host_port}"
        )

        repo_host: DeviceRepoPrx = DeviceRepoPrx.checkedCast(prx)

        self.token = token_hex(8)

        for device in self.devices.values():
            self.logger.info(f"Registering {device.id} to DeviceRepo.")
            repo_host.add_device(
                device.id,
                device.type,
                self.rack,
                self.token,
            )
        self.logger.info(
            f"{len(self.devices)} devices registered in total.")

        repo_host.ice_getConnection().setCloseCallback(
            lambda conn: self._on_lost_connection()
        )

    def _on_lost_connection(self):
        if not self.started:
            return

        self.logger.warning(
            "Lost connection with host. Trying to reconnect...")
        attempts = 1
        while self.started:
            try:
                self.logger.warning(f"Reconnect attempt {attempts}:")
                self._connect_and_register_devices()
                break
            except Ice.ConnectionRefusedException as e:
                self.logger.warning("Attempt failed with exception:")
                self.logger.warning(e)
            except Ice.CommunicatorDestroyedException as e:
                break
            time.sleep(3)
            attempts += 1

    def start(self):
        if self.started:
            return

        if not self.devices:
            self.logger.warning("There is no device to host.")
            return

        self.logger.info("Starting DeviceRack...")

        ice_props = Ice.createProperties()

        ice_props.setProperty("Ice.ThreadPool.Client.Size", "1")
        ice_props.setProperty("Ice.ThreadPool.Client.SizeMax", "10")
        ice_props.setProperty("Ice.ThreadPool.Server.Size", "1")
        ice_props.setProperty("Ice.ThreadPool.Server.SizeMax", "10")

        ice_init_data = Ice.InitializationData()
        ice_init_data.properties = ice_props

        with Ice.initialize(ice_init_data) as ic:
            self.ic = ic
            self.started = True
            self.adapter = ic.createObjectAdapterWithEndpoints(
                "DeviceRackAdapter", "tcp -h 0.0.0.0 -p 0")

            self.rack: DeviceRackPrx = DeviceRackPrx.uncheckedCast(
                self.adapter.add(self, ic.stringToIdentity(self.name))
            )

            self.adapter.activate()
            endpoint_info = self.adapter.getEndpoints()[0].getInfo()
            self.bind_address = endpoint_info.host
            self.bind_port = endpoint_info.port

            self.logger.info(f"DeviceRack started at {self.bind_address}:"
                             f"{self.bind_port}.")

            self._connect_and_register_devices()

            try:
                ic.waitForShutdown()
            except KeyboardInterrupt:
                self.started = False
