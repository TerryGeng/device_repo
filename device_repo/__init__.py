from .device_repo_ice import device_repo_ice as device_repo_ice_
from .device_repo_ice import (device_type_ice, AWG_ice, Dummy_ice, PSG_ice,
                              DCSource_ice, visa_device_ice, VNA_ice, Digitizer_ice)

DeviceType = device_type_ice.DeviceType if hasattr(device_type_ice, "DeviceType") else device_type_ice._M_device_repo_ice.DeviceType
DoubleDataSet = device_type_ice.DoubleDataSet if hasattr(device_type_ice, "DoubleDataSet") else device_type_ice._M_device_repo_ice.DoubleDataSet

DeviceRepo = device_repo_ice_.DeviceRepoPrx if hasattr(device_repo_ice_, "DeviceRepoPrx") else device_repo_ice_._M_device_repo_ice.DeviceRepoPrx
DeviceStatus = device_repo_ice_.DeviceStatus if hasattr(device_repo_ice_, "DeviceStatus") else device_repo_ice_._M_device_repo_ice.DeviceStatus

DeviceOccupiedException = device_repo_ice_.DeviceOccupiedException if hasattr(device_repo_ice_, "DeviceOccupiedException") else device_repo_ice_._M_device_repo_ice.DeviceOccupiedException
UnknownDeviceException = device_repo_ice_.UnknownDeviceException if hasattr(device_repo_ice_, "UnknownDeviceException") else device_repo_ice_._M_device_repo_ice.UnknownDeviceException
DeviceException = device_repo_ice_.DeviceException if hasattr(device_repo_ice_, "DeviceException") else device_repo_ice_._M_device_repo_ice.DeviceException
WrongParameterException = device_repo_ice_.WrongParameterException if hasattr(device_repo_ice_, "WrongParameterException") else device_repo_ice_._M_device_repo_ice.WrongParameterException

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

DigitizerTemplate = Digitizer_ice.Digitizer if hasattr(Digitizer_ice, "Digitizer") else Digitizer_ice._M_device_repo_ice.Digitizer
Digitizer = Digitizer_ice.DigitizerPrx if hasattr(Digitizer_ice, "DigitizerPrx") else Digitizer_ice._M_device_repo_ice.DigitizerPrx

from .access import DeviceRepoAccess
from .rack import DeviceRackI as DeviceRack
