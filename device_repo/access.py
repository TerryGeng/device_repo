import Ice

from .device_repo_ice import (DeviceRepoPrx, DeviceStatus, DeviceType,
                              DummyDevicePrx, AWGPrx, PSGPrx)

DEVICE_MAP = {
    DeviceType.Dummy: DummyDevicePrx,
    DeviceType.ArbitraryWaveformGenerator: AWGPrx,
    DeviceType.ParametricSignalGenerator: PSGPrx
}


class DeviceRepoAccess:
    def __init__(self, host_address, host_port):
        self.host_address = host_address
        self.host_port = host_port

        ice_props = Ice.createProperties()
        ice_props.setProperty("Ice.ACM.Close", "0")  # CloseOff
        # Heartbeat is sent by the server side.
        ice_props.setProperty("Ice.ACM.Heartbeat", "0")  # HeartbeatOff

        ice_init_data = Ice.InitializationData()
        ice_init_data.properties = ice_props

        self.ic = Ice.initialize(ice_init_data)

        self.host: DeviceRepoPrx = DeviceRepoPrx.checkedCast(
            self.ic.stringToProxy(
                f"DeviceRepo:tcp -h {self.host_address} "
                f"-p {self.host_port}"
            )
        )
        self.host.ice_ping()

    def list_device(self):
        return self.host.list_devices()

    def list_device_status(self):
        return [(dev.id, dev.type, self.host.check_device_status(dev.id))
                for dev in self.list_device()]

    def get_device(self, device_id):
        _type = self.host.get_device_type(device_id)
        prx = self.host.acquire_device(device_id)
        return DEVICE_MAP[_type].uncheckedCast(prx)

    def get_device_status(self, device_id):
        return self.host.check_device_status(device_id)

    def release_device(self, device_id):
        return self.host.release_device(device_id)

    def __del__(self):
        self.ic.destroy()
