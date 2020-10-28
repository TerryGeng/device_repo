# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `Dummy.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import device_repo_ice.device_repo_ice

# Included module device_repo_ice
_M_device_repo_ice = Ice.openModule('device_repo_ice')

# Start of module device_repo_ice
__name__ = 'device_repo_ice'

_M_device_repo_ice._t_DummyDevice = IcePy.defineValue('::device_repo_ice::DummyDevice', Ice.Value, -1, (), False, True, None, ())

if 'DummyDevicePrx' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DummyDevicePrx = Ice.createTempClass()
    class DummyDevicePrx(_M_device_repo_ice.DevicePrx):

        def get_data(self, context=None):
            return _M_device_repo_ice.DummyDevice._op_get_data.invoke(self, ((), context))

        def get_dataAsync(self, context=None):
            return _M_device_repo_ice.DummyDevice._op_get_data.invokeAsync(self, ((), context))

        def begin_get_data(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DummyDevice._op_get_data.begin(self, ((), _response, _ex, _sent, context))

        def end_get_data(self, _r):
            return _M_device_repo_ice.DummyDevice._op_get_data.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_device_repo_ice.DummyDevicePrx.ice_checkedCast(proxy, '::device_repo_ice::DummyDevice', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_device_repo_ice.DummyDevicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DummyDevice'
    _M_device_repo_ice._t_DummyDevicePrx = IcePy.defineProxy('::device_repo_ice::DummyDevice', DummyDevicePrx)

    _M_device_repo_ice.DummyDevicePrx = DummyDevicePrx
    del DummyDevicePrx

    _M_device_repo_ice.DummyDevice = Ice.createTempClass()
    class DummyDevice(_M_device_repo_ice.Device):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::device_repo_ice::Device', '::device_repo_ice::DummyDevice')

        def ice_id(self, current=None):
            return '::device_repo_ice::DummyDevice'

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DummyDevice'

        def get_data(self, current=None):
            raise NotImplementedError("servant method 'get_data' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DummyDeviceDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_DummyDeviceDisp = IcePy.defineClass('::device_repo_ice::DummyDevice', DummyDevice, (), None, (_M_device_repo_ice._t_DeviceDisp,))
    DummyDevice._ice_type = _M_device_repo_ice._t_DummyDeviceDisp

    DummyDevice._op_get_data = IcePy.Operation('get_data', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_device_repo_ice._t_bytes, False, 0), ())

    _M_device_repo_ice.DummyDevice = DummyDevice
    del DummyDevice

# End of module device_repo_ice
