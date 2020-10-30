from device_repo.device_repo_ice import Dummy_ice
from device_repo.wrapper.wrapper_base import WrapperBase
DummyDevice = Dummy_ice.DummyDevicePrx if hasattr(Dummy_ice, "DummyDevicePrx") else Dummy_ice._M_device_repo_ice.DummyDevicePrx


class DummyWrapper(WrapperBase):
    def __init__(self, base):
        super().__init__(base)

    @staticmethod
    def checkedCast(proxy, facetOrContext=None, context=None):
        return DummyWrapper(DummyDevice.checkedCast(proxy, facetOrContext, context))

    @staticmethod
    def uncheckedCast(proxy, facet=None):
        return DummyWrapper(DummyDevice.uncheckedCast(proxy, facet))

    # -----------------------
    #    Extended method
    # -----------------------

    def get_string_data(self):
        return self.get_data().decode("utf-8")

