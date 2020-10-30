# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `device_type.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module device_repo_ice
_M_device_repo_ice = Ice.openModule('device_repo.device_repo_ice')
__name__ = 'device_repo.device_repo_ice'

if 'DeviceType' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceType = Ice.createTempClass()
    class DeviceType(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    DeviceType.Dummy = DeviceType("Dummy", 0)
    DeviceType.ArbitraryWaveformGenerator = DeviceType("ArbitraryWaveformGenerator", 1)
    DeviceType.ParametricSignalGenerator = DeviceType("ParametricSignalGenerator", 2)
    DeviceType.Acquisition = DeviceType("Acquisition", 3)
    DeviceType.VectorNetworkAnalyzer = DeviceType("VectorNetworkAnalyzer", 4)
    DeviceType.DelayGenerator = DeviceType("DelayGenerator", 5)
    DeviceType.DCSource = DeviceType("DCSource", 6)
    DeviceType._enumerators = { 0:DeviceType.Dummy, 1:DeviceType.ArbitraryWaveformGenerator, 2:DeviceType.ParametricSignalGenerator, 3:DeviceType.Acquisition, 4:DeviceType.VectorNetworkAnalyzer, 5:DeviceType.DelayGenerator, 6:DeviceType.DCSource }

    _M_device_repo_ice._t_DeviceType = IcePy.defineEnum('::device_repo_ice::DeviceType', DeviceType, (), DeviceType._enumerators)

    _M_device_repo_ice.DeviceType = DeviceType
    del DeviceType

# End of module device_repo_ice
