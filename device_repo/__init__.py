from .device_repo_ice import AWG_ice, Dummy_ice, host_ice
from .access import DeviceRepoAccess
from .device_rack import DeviceRackI as DeviceRack
from .host import DeviceRepo

DeviceType = host_ice._M_device_repo_ice.DeviceType
DeviceStatus = host_ice._M_device_repo_ice.DeviceStatus

DeviceOccupiedException = host_ice._M_device_repo_ice.DeviceOccupiedException
UnknownDeviceException = host_ice._M_device_repo_ice.UnknownDeviceException

AWGTemplate = AWG_ice._M_device_repo_ice.AWG
AWG = AWG_ice._M_device_repo_ice.AWGPrx
DummyDeviceTemplate = Dummy_ice._M_device_repo_ice.DummyDevice
DummyDevice = Dummy_ice._M_device_repo_ice.DummyDevicePrx
