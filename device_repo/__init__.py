from .device_repo_ice import (device_repo_ice, AWG_ice, Dummy_ice, PSG_ice,
                   DCSource_ice, visa_device_ice, VNA_ice)

DeviceRepo = device_repo_ice.DeviceRepoPrx if hasattr(device_repo_ice, "DeviceRepoPrx") else device_repo_ice._M_device_repo_ice.DeviceRepoPrx

DeviceType = device_repo_ice.DeviceType if hasattr(device_repo_ice, "DeviceType") else device_repo_ice._M_device_repo_ice.DeviceType
DeviceStatus = device_repo_ice.DeviceStatus if hasattr(device_repo_ice, "DeviceStatus") else device_repo_ice._M_device_repo_ice.DeviceStatus

DeviceOccupiedException = device_repo_ice._M_device_repo_ice.DeviceOccupiedException
UnknownDeviceException = device_repo_ice._M_device_repo_ice.UnknownDeviceException

VisaDeviceTemplate = visa_device_ice.VisaDevice if hasattr(visa_device_ice, "VisaDevice") else visa_device_ice._M_device_repo_ice.VisaDevice
VisaDevice = visa_device_ice.VisaDevicePrx if hasattr(visa_device_ice, "VisaDevicePrx") else visa_device_ice._M_device_repo_ice.VisaDevicePrx

from .wrapper.dummy_wrapper import DummyWrapper
DummyDeviceTemplate = Dummy_ice.DummyDevice if hasattr(Dummy_ice, "DummyDevice") else Dummy_ice._M_device_repo_ice.DummyDevice
DummyDevice = DummyWrapper

AWGTemplate = AWG_ice.AWG if hasattr(AWG_ice, "AWG") else AWG_ice._M_device_repo_ice.AWG
AWG = AWG_ice.AWGPrx if hasattr(AWG_ice, "AWGPrx") else AWG_ice._M_device_repo_ice.AWGPrx

PSGTemplate = PSG_ice.PSG if hasattr(PSG_ice, "PSG") else PSG_ice._M_device_repo_ice.PSG
PSG = PSG_ice.PSGPrx if hasattr(PSG_ice, "PSGPrx") else PSG_ice._M_device_repo_ice.PSGPrx

DCSourceTemplate = DCSource_ice.DCSource if hasattr(DCSource_ice, "DCSource") else DCSource_ice._M_device_repo_ice.DCSource
DCSource = DCSource_ice.DCSourcePrx if hasattr(DCSource_ice, "DCSourcePrx") else DCSource_ice._M_device_repo_ice.DCSourcePrx

from .wrapper.vna_wrapper import VNAWrapper
VNATemplate = VNA_ice.VNA if hasattr(VNA_ice, "VNA") else VNA_ice._M_device_repo_ice.VNA
VNA = VNAWrapper

from .access import DeviceRepoAccess
from .rack import DeviceRackI as DeviceRack
