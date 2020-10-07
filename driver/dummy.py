from device_repo import DummyDeviceTemplate, DeviceType


class DummyDev(DummyDeviceTemplate):
    def __init__(self):
        pass

    def get_type(self, current=None):
        return DeviceType.Dummy

    def get_data(self, current=None):
        return b"Hello world!"
