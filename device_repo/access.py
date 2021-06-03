import Ice

from device_repo import (DeviceType, DeviceRepo, DeviceStatus, DummyDevice,
                         AWG, PSG, VNA, Digitizer, DG, DCSource,
                         DeviceReacquiredException)

DEVICE_MAP = {
    DeviceType.Dummy: DummyDevice,
    DeviceType.ArbitraryWaveformGenerator: AWG,
    DeviceType.ParametricSignalGenerator: PSG,
    DeviceType.VectorNetworkAnalyzer: VNA,
    DeviceType.Digitizer: Digitizer,
    DeviceType.DelayGenerator: DG,
    DeviceType.DCSource: DCSource
}


class DeviceRepoAccess:
    def __init__(self, host_address, host_port):
        self.host_address = host_address
        self.host_port = host_port

        ice_props = Ice.createProperties()
        ice_props.setProperty("Ice.ACM.Close", "0")  # CloseOff
        # Heartbeat is sent by the server side.
        ice_props.setProperty("Ice.ACM.Heartbeat", "0")  # HeartbeatOff
        ice_props.setProperty("Ice.MessageSizeMax", "20000")  # 20MB

        ice_init_data = Ice.InitializationData()
        ice_init_data.properties = ice_props

        self.ic = Ice.initialize(ice_init_data)

        self.host: DeviceRepo = DeviceRepo.checkedCast(
            self.ic.stringToProxy(
                f"DeviceRepo:tcp -h {self.host_address} "
                f"-p {self.host_port}"
            )
        )
        self.host.ice_ping()

        self.id_prx_map = {}

    def list_device(self):
        return self.host.list_devices()

    def list_device_status(self):
        return [(dev.id, dev.type, self.host.check_device_status(dev.id))
                for dev in self.list_device()]

    def get_device(self, device_id):
        _type = self.host.get_device_type(device_id)
        try:
            prx = DEVICE_MAP[_type].uncheckedCast(self.host.acquire_device(device_id))
            self.id_prx_map[device_id] = prx
        except DeviceReacquiredException:
            assert device_id in self.id_prx_map, "Sanity check failed. This is a bug."
            prx = self.id_prx_map[device_id]

        return prx

    def get_device_status(self, device_id):
        return self.host.check_device_status(device_id)

    def release_device(self, dev):
        dev_id = ""
        if isinstance(dev, str):
            dev_id = dev
        else:
            for _id, prx in self.id_prx_map.items():
                if prx == dev:
                    dev_id = _id
                    break
            if not dev_id:
                return True

        del self.id_prx_map[dev_id]
        return self.host.release_device(dev_id)

    def list_acquired_devices(self):
        return [(dev.id, dev.type, self.host.check_device_status(dev.id))
                for dev in self.host.list_acquired_devices()]

    def release_all(self):
        for _id, _, _ in self.list_acquired_devices():
            self.host.release_device(_id)
        self.id_prx_map = {}

    def __del__(self):
        self.ic.destroy()
