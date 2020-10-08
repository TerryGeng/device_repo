from .device_repo_ice import AWG_ice, Dummy_ice, device_repo_ice
from .access import DeviceRepoAccess
from .rack import DeviceRackI as DeviceRack

DeviceType = device_repo_ice._M_device_repo_ice.DeviceType
DeviceStatus = device_repo_ice._M_device_repo_ice.DeviceStatus

DeviceOccupiedException = device_repo_ice._M_device_repo_ice.DeviceOccupiedException
UnknownDeviceException = device_repo_ice._M_device_repo_ice.UnknownDeviceException

AWGTemplate = AWG_ice._M_device_repo_ice.AWG
AWG = AWG_ice._M_device_repo_ice.AWGPrx
DummyDeviceTemplate = Dummy_ice._M_device_repo_ice.DummyDevice
DummyDevice = Dummy_ice._M_device_repo_ice.DummyDevicePrx
