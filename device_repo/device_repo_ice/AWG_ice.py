# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `AWG.ice'
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

if '_t_RawWaveform' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_RawWaveform = IcePy.defineSequence('::device_repo_ice::RawWaveform', (), IcePy._t_double)

_M_device_repo_ice._t_AWG = IcePy.defineValue('::device_repo_ice::AWG', Ice.Value, -1, (), False, True, None, ())

if 'AWGPrx' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.AWGPrx = Ice.createTempClass()
    class AWGPrx(_M_device_repo_ice.DevicePrx):

        def get_sample_rate(self, context=None):
            return _M_device_repo_ice.AWG._op_get_sample_rate.invoke(self, ((), context))

        def get_sample_rateAsync(self, context=None):
            return _M_device_repo_ice.AWG._op_get_sample_rate.invokeAsync(self, ((), context))

        def begin_get_sample_rate(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_get_sample_rate.begin(self, ((), _response, _ex, _sent, context))

        def end_get_sample_rate(self, _r):
            return _M_device_repo_ice.AWG._op_get_sample_rate.end(self, _r)

        def write_raw_waveform(self, waveform, amplitude, context=None):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.invoke(self, ((waveform, amplitude), context))

        def write_raw_waveformAsync(self, waveform, amplitude, context=None):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.invokeAsync(self, ((waveform, amplitude), context))

        def begin_write_raw_waveform(self, waveform, amplitude, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.begin(self, ((waveform, amplitude), _response, _ex, _sent, context))

        def end_write_raw_waveform(self, _r):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.end(self, _r)

        def set_offset(self, amplitude, offset_voltage, context=None):
            return _M_device_repo_ice.AWG._op_set_offset.invoke(self, ((amplitude, offset_voltage), context))

        def set_offsetAsync(self, amplitude, offset_voltage, context=None):
            return _M_device_repo_ice.AWG._op_set_offset.invokeAsync(self, ((amplitude, offset_voltage), context))

        def begin_set_offset(self, amplitude, offset_voltage, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_set_offset.begin(self, ((amplitude, offset_voltage), _response, _ex, _sent, context))

        def end_set_offset(self, _r):
            return _M_device_repo_ice.AWG._op_set_offset.end(self, _r)

        def set_amplitude(self, amp_in_volts, context=None):
            return _M_device_repo_ice.AWG._op_set_amplitude.invoke(self, ((amp_in_volts, ), context))

        def set_amplitudeAsync(self, amp_in_volts, context=None):
            return _M_device_repo_ice.AWG._op_set_amplitude.invokeAsync(self, ((amp_in_volts, ), context))

        def begin_set_amplitude(self, amp_in_volts, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_set_amplitude.begin(self, ((amp_in_volts, ), _response, _ex, _sent, context))

        def end_set_amplitude(self, _r):
            return _M_device_repo_ice.AWG._op_set_amplitude.end(self, _r)

        def stop(self, context=None):
            return _M_device_repo_ice.AWG._op_stop.invoke(self, ((), context))

        def stopAsync(self, context=None):
            return _M_device_repo_ice.AWG._op_stop.invokeAsync(self, ((), context))

        def begin_stop(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_stop.begin(self, ((), _response, _ex, _sent, context))

        def end_stop(self, _r):
            return _M_device_repo_ice.AWG._op_stop.end(self, _r)

        def run(self, context=None):
            return _M_device_repo_ice.AWG._op_run.invoke(self, ((), context))

        def runAsync(self, context=None):
            return _M_device_repo_ice.AWG._op_run.invokeAsync(self, ((), context))

        def begin_run(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_run.begin(self, ((), _response, _ex, _sent, context))

        def end_run(self, _r):
            return _M_device_repo_ice.AWG._op_run.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_device_repo_ice.AWGPrx.ice_checkedCast(proxy, '::device_repo_ice::AWG', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_device_repo_ice.AWGPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::AWG'
    _M_device_repo_ice._t_AWGPrx = IcePy.defineProxy('::device_repo_ice::AWG', AWGPrx)

    _M_device_repo_ice.AWGPrx = AWGPrx
    del AWGPrx

    _M_device_repo_ice.AWG = Ice.createTempClass()
    class AWG(_M_device_repo_ice.Device):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::device_repo_ice::AWG', '::device_repo_ice::Device')

        def ice_id(self, current=None):
            return '::device_repo_ice::AWG'

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::AWG'

        def get_sample_rate(self, current=None):
            raise NotImplementedError("servant method 'get_sample_rate' not implemented")

        def write_raw_waveform(self, waveform, amplitude, current=None):
            raise NotImplementedError("servant method 'write_raw_waveform' not implemented")

        def set_offset(self, amplitude, offset_voltage, current=None):
            raise NotImplementedError("servant method 'set_offset' not implemented")

        def set_amplitude(self, amp_in_volts, current=None):
            raise NotImplementedError("servant method 'set_amplitude' not implemented")

        def stop(self, current=None):
            raise NotImplementedError("servant method 'stop' not implemented")

        def run(self, current=None):
            raise NotImplementedError("servant method 'run' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_AWGDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_AWGDisp = IcePy.defineClass('::device_repo_ice::AWG', AWG, (), None, (_M_device_repo_ice._t_DeviceDisp,))
    AWG._ice_type = _M_device_repo_ice._t_AWGDisp

    AWG._op_get_sample_rate = IcePy.Operation('get_sample_rate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_double, False, 0), ())
    AWG._op_write_raw_waveform = IcePy.Operation('write_raw_waveform', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_device_repo_ice._t_RawWaveform, False, 0), ((), IcePy._t_double, False, 0)), (), None, ())
    AWG._op_set_offset = IcePy.Operation('set_offset', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)), (), None, ())
    AWG._op_set_amplitude = IcePy.Operation('set_amplitude', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0),), (), None, ())
    AWG._op_stop = IcePy.Operation('stop', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    AWG._op_run = IcePy.Operation('run', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_device_repo_ice.AWG = AWG
    del AWG

# End of module device_repo_ice
