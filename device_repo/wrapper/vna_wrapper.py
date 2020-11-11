from device_repo.device_repo_ice import VNA_ice
from device_repo.wrapper.wrapper_base import WrapperBase
VNAPrx = VNA_ice.VNAPrx if hasattr(VNA_ice, "VNAPrx") else VNA_ice._M_device_repo_ice.VNAPrx


class VNAWrapper(WrapperBase):
    base_type = VNAPrx

    def __init__(self, base: VNAPrx):
        super().__init__(base)

    def get_s(self, channel=1, context=None):
        ret = self.base.get_s(channel, context)
        reals = ret[::2]
        imags = ret[1::2]
        complex_ret = [real + 1j*imag for real, imag in zip(reals, imags)]
        return complex_ret
