# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `DCSource.ice'
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

_M_device_repo_ice._t_DCSource = IcePy.defineValue('::device_repo_ice::DCSource', Ice.Value, -1, (), False, True, None, ())

if 'DCSourcePrx' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DCSourcePrx = Ice.createTempClass()
    class DCSourcePrx(_M_device_repo_ice.DevicePrx):

        def set_voltage(self, voltage_in_volts, context=None):
            return _M_device_repo_ice.DCSource._op_set_voltage.invoke(self, ((voltage_in_volts, ), context))

        def set_voltageAsync(self, voltage_in_volts, context=None):
            return _M_device_repo_ice.DCSource._op_set_voltage.invokeAsync(self, ((voltage_in_volts, ), context))

        def begin_set_voltage(self, voltage_in_volts, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DCSource._op_set_voltage.begin(self, ((voltage_in_volts, ), _response, _ex, _sent, context))

        def end_set_voltage(self, _r):
            return _M_device_repo_ice.DCSource._op_set_voltage.end(self, _r)

        def get_voltage(self, context=None):
            return _M_device_repo_ice.DCSource._op_get_voltage.invoke(self, ((), context))

        def get_voltageAsync(self, context=None):
            return _M_device_repo_ice.DCSource._op_get_voltage.invokeAsync(self, ((), context))

        def begin_get_voltage(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DCSource._op_get_voltage.begin(self, ((), _response, _ex, _sent, context))

        def end_get_voltage(self, _r):
            return _M_device_repo_ice.DCSource._op_get_voltage.end(self, _r)

        def output_on(self, context=None):
            return _M_device_repo_ice.DCSource._op_output_on.invoke(self, ((), context))

        def output_onAsync(self, context=None):
            return _M_device_repo_ice.DCSource._op_output_on.invokeAsync(self, ((), context))

        def begin_output_on(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DCSource._op_output_on.begin(self, ((), _response, _ex, _sent, context))

        def end_output_on(self, _r):
            return _M_device_repo_ice.DCSource._op_output_on.end(self, _r)

        def output_off(self, context=None):
            return _M_device_repo_ice.DCSource._op_output_off.invoke(self, ((), context))

        def output_offAsync(self, context=None):
            return _M_device_repo_ice.DCSource._op_output_off.invokeAsync(self, ((), context))

        def begin_output_off(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DCSource._op_output_off.begin(self, ((), _response, _ex, _sent, context))

        def end_output_off(self, _r):
            return _M_device_repo_ice.DCSource._op_output_off.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_device_repo_ice.DCSourcePrx.ice_checkedCast(proxy, '::device_repo_ice::DCSource', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_device_repo_ice.DCSourcePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DCSource'
    _M_device_repo_ice._t_DCSourcePrx = IcePy.defineProxy('::device_repo_ice::DCSource', DCSourcePrx)

    _M_device_repo_ice.DCSourcePrx = DCSourcePrx
    del DCSourcePrx

    _M_device_repo_ice.DCSource = Ice.createTempClass()
    class DCSource(_M_device_repo_ice.Device):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::device_repo_ice::DCSource', '::device_repo_ice::Device')

        def ice_id(self, current=None):
            return '::device_repo_ice::DCSource'

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DCSource'

        def set_voltage(self, voltage_in_volts, current=None):
            raise NotImplementedError("servant method 'set_voltage' not implemented")

        def get_voltage(self, current=None):
            raise NotImplementedError("servant method 'get_voltage' not implemented")

        def output_on(self, current=None):
            raise NotImplementedError("servant method 'output_on' not implemented")

        def output_off(self, current=None):
            raise NotImplementedError("servant method 'output_off' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DCSourceDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_DCSourceDisp = IcePy.defineClass('::device_repo_ice::DCSource', DCSource, (), None, (_M_device_repo_ice._t_DeviceDisp,))
    DCSource._ice_type = _M_device_repo_ice._t_DCSourceDisp

    DCSource._op_set_voltage = IcePy.Operation('set_voltage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0),), (), None, ())
    DCSource._op_get_voltage = IcePy.Operation('get_voltage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_double, False, 0), ())
    DCSource._op_output_on = IcePy.Operation('output_on', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    DCSource._op_output_off = IcePy.Operation('output_off', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_device_repo_ice.DCSource = DCSource
    del DCSource

# End of module device_repo_ice
