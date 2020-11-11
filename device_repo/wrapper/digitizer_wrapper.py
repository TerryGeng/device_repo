from device_repo.device_repo_ice import Digitizer_ice
from device_repo.wrapper.wrapper_base import WrapperBase
from device_repo.utils import unpack_data_set
DigitizerPrx = Digitizer_ice.DigitizerPrx if hasattr(Digitizer_ice, "DigitizerPrx") \
    else Digitizer_ice._M_device_repo_ice.DigitizerPrx


class DigitizerWrapper(WrapperBase):
    base_type = DigitizerPrx

    def __init__(self, base):
        super().__init__(base)

    def acquire_and_fetch(self):
        dst = self.base.acquire_and_fetch()
        return unpack_data_set(dst)

    def fetch_data(self):
        dst = self.base.fetch_data()
        return unpack_data_set(dst)

