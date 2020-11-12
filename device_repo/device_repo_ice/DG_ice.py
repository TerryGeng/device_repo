# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `DG.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
from . import device_repo_ice

# Included module device_repo_ice
_M_device_repo_ice = Ice.openModule('device_repo.device_repo_ice')

# Start of module device_repo_ice
__name__ = 'device_repo.device_repo_ice'

_M_device_repo_ice._t_DG = IcePy.defineValue('::device_repo_ice::DG', Ice.Value, -1, (), False, True, None, ())

if 'DGPrx' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DGPrx = Ice.createTempClass()
    class DGPrx(_M_device_repo_ice.DevicePrx):

        def set_cycle_frequency(self, freq_in_hz, context=None):
            return _M_device_repo_ice.DG._op_set_cycle_frequency.invoke(self, ((freq_in_hz, ), context))

        def set_cycle_frequencyAsync(self, freq_in_hz, context=None):
            return _M_device_repo_ice.DG._op_set_cycle_frequency.invokeAsync(self, ((freq_in_hz, ), context))

        def begin_set_cycle_frequency(self, freq_in_hz, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DG._op_set_cycle_frequency.begin(self, ((freq_in_hz, ), _response, _ex, _sent, context))

        def end_set_cycle_frequency(self, _r):
            return _M_device_repo_ice.DG._op_set_cycle_frequency.end(self, _r)

        def get_cycle_frequency(self, context=None):
            return _M_device_repo_ice.DG._op_get_cycle_frequency.invoke(self, ((), context))

        def get_cycle_frequencyAsync(self, context=None):
            return _M_device_repo_ice.DG._op_get_cycle_frequency.invokeAsync(self, ((), context))

        def begin_get_cycle_frequency(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DG._op_get_cycle_frequency.begin(self, ((), _response, _ex, _sent, context))

        def end_get_cycle_frequency(self, _r):
            return _M_device_repo_ice.DG._op_get_cycle_frequency.end(self, _r)

        def set_channel_delay(self, channel_index, rising_at, fall_after, context=None):
            return _M_device_repo_ice.DG._op_set_channel_delay.invoke(self, ((channel_index, rising_at, fall_after), context))

        def set_channel_delayAsync(self, channel_index, rising_at, fall_after, context=None):
            return _M_device_repo_ice.DG._op_set_channel_delay.invokeAsync(self, ((channel_index, rising_at, fall_after), context))

        def begin_set_channel_delay(self, channel_index, rising_at, fall_after, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DG._op_set_channel_delay.begin(self, ((channel_index, rising_at, fall_after), _response, _ex, _sent, context))

        def end_set_channel_delay(self, _r):
            return _M_device_repo_ice.DG._op_set_channel_delay.end(self, _r)

        def get_channel_delay(self, channel_index, context=None):
            return _M_device_repo_ice.DG._op_get_channel_delay.invoke(self, ((channel_index, ), context))

        def get_channel_delayAsync(self, channel_index, context=None):
            return _M_device_repo_ice.DG._op_get_channel_delay.invokeAsync(self, ((channel_index, ), context))

        def begin_get_channel_delay(self, channel_index, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DG._op_get_channel_delay.begin(self, ((channel_index, ), _response, _ex, _sent, context))

        def end_get_channel_delay(self, _r):
            return _M_device_repo_ice.DG._op_get_channel_delay.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_device_repo_ice.DGPrx.ice_checkedCast(proxy, '::device_repo_ice::DG', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_device_repo_ice.DGPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DG'
    _M_device_repo_ice._t_DGPrx = IcePy.defineProxy('::device_repo_ice::DG', DGPrx)

    _M_device_repo_ice.DGPrx = DGPrx
    del DGPrx

    _M_device_repo_ice.DG = Ice.createTempClass()
    class DG(_M_device_repo_ice.Device):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::device_repo_ice::DG', '::device_repo_ice::Device')

        def ice_id(self, current=None):
            return '::device_repo_ice::DG'

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DG'

        def set_cycle_frequency(self, freq_in_hz, current=None):
            raise NotImplementedError("servant method 'set_cycle_frequency' not implemented")

        def get_cycle_frequency(self, current=None):
            raise NotImplementedError("servant method 'get_cycle_frequency' not implemented")

        def set_channel_delay(self, channel_index, rising_at, fall_after, current=None):
            raise NotImplementedError("servant method 'set_channel_delay' not implemented")

        def get_channel_delay(self, channel_index, current=None):
            raise NotImplementedError("servant method 'get_channel_delay' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DGDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_DGDisp = IcePy.defineClass('::device_repo_ice::DG', DG, (), None, (_M_device_repo_ice._t_DeviceDisp,))
    DG._ice_type = _M_device_repo_ice._t_DGDisp

    DG._op_set_cycle_frequency = IcePy.Operation('set_cycle_frequency', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0),), (), None, ())
    DG._op_get_cycle_frequency = IcePy.Operation('get_cycle_frequency', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_double, False, 0), ())
    DG._op_set_channel_delay = IcePy.Operation('set_channel_delay', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)), (), None, ())
    DG._op_get_channel_delay = IcePy.Operation('get_channel_delay', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), ((), _M_device_repo_ice._t_ints, False, 0), ())

    _M_device_repo_ice.DG = DG
    del DG

# End of module device_repo_ice
