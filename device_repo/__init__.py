from .device_repo_ice import device_repo_ice, AWG_ice, Dummy_ice, PSG_ice, DCSource_ice, visa_device_ice
from .access import DeviceRepoAccess
from .rack import DeviceRackI as DeviceRack

DeviceType = device_repo_ice._M_device_repo_ice.DeviceType
DeviceStatus = device_repo_ice._M_device_repo_ice.DeviceStatus

DeviceOccupiedException = device_repo_ice._M_device_repo_ice.DeviceOccupiedException
UnknownDeviceException = device_repo_ice._M_device_repo_ice.UnknownDeviceException

VisaDeviceTemplate = visa_device_ice._M_device_repo_ice.VisaDevice
VisaDevice = visa_device_ice._M_device_repo_ice.VisaDevicePrx

DummyDeviceTemplate = Dummy_ice._M_device_repo_ice.DummyDevice
DummyDevice = Dummy_ice._M_device_repo_ice.DummyDevicePrx

AWGTemplate = AWG_ice._M_device_repo_ice.AWG
AWG = AWG_ice._M_device_repo_ice.AWGPrx
PSGTemplate = PSG_ice._M_device_repo_ice.PSG
PSG = PSG_ice._M_device_repo_ice.PSGPrx
DCSourceTemplate = DCSource_ice._M_device_repo_ice.DCSource
DCSource = DCSource_ice._M_device_repo_ice.DCSourcePrx
