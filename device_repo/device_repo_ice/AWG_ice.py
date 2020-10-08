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

        def write_raw_waveform(self, channel, amplitude, waveform, context=None):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.invoke(self, ((channel, amplitude, waveform), context))

        def write_raw_waveformAsync(self, channel, amplitude, waveform, context=None):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.invokeAsync(self, ((channel, amplitude, waveform), context))

        def begin_write_raw_waveform(self, channel, amplitude, waveform, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.begin(self, ((channel, amplitude, waveform), _response, _ex, _sent, context))

        def end_write_raw_waveform(self, _r):
            return _M_device_repo_ice.AWG._op_write_raw_waveform.end(self, _r)

        def set_channel_offset(self, channel, amplitude, offset_voltage, context=None):
            return _M_device_repo_ice.AWG._op_set_channel_offset.invoke(self, ((channel, amplitude, offset_voltage), context))

        def set_channel_offsetAsync(self, channel, amplitude, offset_voltage, context=None):
            return _M_device_repo_ice.AWG._op_set_channel_offset.invokeAsync(self, ((channel, amplitude, offset_voltage), context))

        def begin_set_channel_offset(self, channel, amplitude, offset_voltage, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_set_channel_offset.begin(self, ((channel, amplitude, offset_voltage), _response, _ex, _sent, context))

        def end_set_channel_offset(self, _r):
            return _M_device_repo_ice.AWG._op_set_channel_offset.end(self, _r)

        def set_channel_amplitude(self, channel, amp_in_volts, context=None):
            return _M_device_repo_ice.AWG._op_set_channel_amplitude.invoke(self, ((channel, amp_in_volts), context))

        def set_channel_amplitudeAsync(self, channel, amp_in_volts, context=None):
            return _M_device_repo_ice.AWG._op_set_channel_amplitude.invokeAsync(self, ((channel, amp_in_volts), context))

        def begin_set_channel_amplitude(self, channel, amp_in_volts, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_set_channel_amplitude.begin(self, ((channel, amp_in_volts), _response, _ex, _sent, context))

        def end_set_channel_amplitude(self, _r):
            return _M_device_repo_ice.AWG._op_set_channel_amplitude.end(self, _r)

        def stop_all(self, context=None):
            return _M_device_repo_ice.AWG._op_stop_all.invoke(self, ((), context))

        def stop_allAsync(self, context=None):
            return _M_device_repo_ice.AWG._op_stop_all.invokeAsync(self, ((), context))

        def begin_stop_all(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_stop_all.begin(self, ((), _response, _ex, _sent, context))

        def end_stop_all(self, _r):
            return _M_device_repo_ice.AWG._op_stop_all.end(self, _r)

        def run_all(self, context=None):
            return _M_device_repo_ice.AWG._op_run_all.invoke(self, ((), context))

        def run_allAsync(self, context=None):
            return _M_device_repo_ice.AWG._op_run_all.invokeAsync(self, ((), context))

        def begin_run_all(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_run_all.begin(self, ((), _response, _ex, _sent, context))

        def end_run_all(self, _r):
            return _M_device_repo_ice.AWG._op_run_all.end(self, _r)

        def stop_channel(self, channel, context=None):
            return _M_device_repo_ice.AWG._op_stop_channel.invoke(self, ((channel, ), context))

        def stop_channelAsync(self, channel, context=None):
            return _M_device_repo_ice.AWG._op_stop_channel.invokeAsync(self, ((channel, ), context))

        def begin_stop_channel(self, channel, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_stop_channel.begin(self, ((channel, ), _response, _ex, _sent, context))

        def end_stop_channel(self, _r):
            return _M_device_repo_ice.AWG._op_stop_channel.end(self, _r)

        def run_channel(self, channel, context=None):
            return _M_device_repo_ice.AWG._op_run_channel.invoke(self, ((channel, ), context))

        def run_channelAsync(self, channel, context=None):
            return _M_device_repo_ice.AWG._op_run_channel.invokeAsync(self, ((channel, ), context))

        def begin_run_channel(self, channel, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.AWG._op_run_channel.begin(self, ((channel, ), _response, _ex, _sent, context))

        def end_run_channel(self, _r):
            return _M_device_repo_ice.AWG._op_run_channel.end(self, _r)

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

        def write_raw_waveform(self, channel, amplitude, waveform, current=None):
            raise NotImplementedError("servant method 'write_raw_waveform' not implemented")

        def set_channel_offset(self, channel, amplitude, offset_voltage, current=None):
            raise NotImplementedError("servant method 'set_channel_offset' not implemented")

        def set_channel_amplitude(self, channel, amp_in_volts, current=None):
            raise NotImplementedError("servant method 'set_channel_amplitude' not implemented")

        def stop_all(self, current=None):
            raise NotImplementedError("servant method 'stop_all' not implemented")

        def run_all(self, current=None):
            raise NotImplementedError("servant method 'run_all' not implemented")

        def stop_channel(self, channel, current=None):
            raise NotImplementedError("servant method 'stop_channel' not implemented")

        def run_channel(self, channel, current=None):
            raise NotImplementedError("servant method 'run_channel' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_AWGDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_AWGDisp = IcePy.defineClass('::device_repo_ice::AWG', AWG, (), None, (_M_device_repo_ice._t_DeviceDisp,))
    AWG._ice_type = _M_device_repo_ice._t_AWGDisp

    AWG._op_write_raw_waveform = IcePy.Operation('write_raw_waveform', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_double, False, 0), ((), _M_device_repo_ice._t_RawWaveform, False, 0)), (), None, ())
    AWG._op_set_channel_offset = IcePy.Operation('set_channel_offset', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)), (), None, ())
    AWG._op_set_channel_amplitude = IcePy.Operation('set_channel_amplitude', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_double, False, 0)), (), None, ())
    AWG._op_stop_all = IcePy.Operation('stop_all', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    AWG._op_run_all = IcePy.Operation('run_all', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    AWG._op_stop_channel = IcePy.Operation('stop_channel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())
    AWG._op_run_channel = IcePy.Operation('run_channel', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())

    _M_device_repo_ice.AWG = AWG
    del AWG

# End of module device_repo_ice
