from device_repo.utils import (get_logger, get_rack_argv_parser, log_invoke_evt,
                               InvalidParameterException)
from device_repo import (DigitizerTemplate, DeviceException, WrongParameterException,
                         DataSet, DeviceType, DeviceRack)
from device_repo.utils import pack_data_set

import logging
import time

import numpy as np
import re

if __name__ == "__main__":
    from driver.alazar.api import *
    from driver.alazar.constants import *
    from driver.alazar.error_code import *
else:
    from racks.driver.alazar.api import *
    from racks.driver.alazar.constants import *
    from racks.driver.alazar.error_code import *


# The rack program of Alazar's AWG series.
# I tried to call all Alazar's API without any wrapping to
#  1. avoid unnecessary confusion,
#  2. help other reader navigate through Alazar's SDK manual,
# But basically the adversary effect is this piece of code is a
# mixture of traditional python code and "C-style" code.

# Note on sample, record and buffer:
#  Sample is a numeric value, indicate the amplitude of the signal at one
#  specific time. Each record is comprised of a number of records.
#  Alazar device takes one record after being triggered once. The record
#  is saved directly to the on-board buffer of the device.
#  Users can specify the number of records saved in one buffer, and
#  fetch back that buffer after that buffer is completed (is filled
#  by records). You CANNOT fetch data back unless the buffer is completed.
#
#  Number of samples per record = samples_per_record (each channel) * channels
#  Total number of records we get = records_per_buffer
#  Total number of samples we get = records_per_buffer * samples_per_channel * channels


class Alazar(DigitizerTemplate):
    def __init__(self, name, addr, *,
                 samples_per_record=1024,
                 repeats=512,
                 channel_ranges=(0, 0),
                 trigger_level=1.0,
                 trigger_delay=0.0,
                 trigger_timeout=0.0,
                 records_per_buffer=128,
                 read_timeout=1):
        super().__init__()

        self.name = name
        self.addr = addr
        dict_parse = self._parse_addr(self.addr)

        self.model = dict_parse.get('model', None)
        self.system_id = dict_parse.get('systemID', 1)
        self.board_id = dict_parse.get('boardID', 1)
        self.handle = AlazarGetBoardBySystemID(self.system_id, self.board_id)

        self.samples_per_record = self.align_samples_per_record(samples_per_record)
        self.records_per_buffer = records_per_buffer
        self.repeats = repeats
        self.trigger_level = trigger_level
        self.trigger_delay = trigger_delay
        self.trigger_timeout = trigger_timeout
        self.read_timeout = read_timeout
        self.sample_rate = 1000000000

        self.channel_ranges = channel_ranges

        self.initialize()

    def initialize(self):
        assert AlazarSetCaptureClock(
            self.handle, EXTERNAL_CLOCK_10MHz_REF, self.sample_rate, CLOCK_EDGE_RISING, U32(1)) == ApiSuccess
        assert AlazarInputControl(
            self.handle, CHANNEL_A, AC_COUPLING, INPUT_RANGE_PM_100_MV, IMPEDANCE_50_OHM) == ApiSuccess
        assert AlazarInputControl(
            self.handle, CHANNEL_B, AC_COUPLING, INPUT_RANGE_PM_100_MV, IMPEDANCE_50_OHM) == ApiSuccess
        assert AlazarSetExternalTrigger(self.handle, DC_COUPLING, ETR_5V) == ApiSuccess
        assert AlazarSetParameter(self.handle, CHANNEL_A | CHANNEL_B, SET_DATA_FORMAT, DATA_FORMAT_UNSIGNED) == ApiSuccess
        assert AlazarConfigureAuxIO(self.handle, AUX_OUT_TRIGGER, AUX_OUT_TRIGGER_ENABLE) == ApiSuccess

        self.set_trigger_level(self.trigger_level)
        self.set_trigger_delay(self.trigger_delay)
        self.set_trigger_timeout(self.trigger_timeout)

    def get_type(self, current=None):
        return DeviceType.Digitizer

    @log_invoke_evt
    def set_sample_number(self, number_of_samples, current=None):
        self.samples_per_record = self.align_samples_per_record(number_of_samples)

    @log_invoke_evt
    def set_input_range(self, channel, _range, current=None):
        if channel not in [1, 2]:
            raise WrongParameterException(
                "There are only two channels: channel 0 and channel 1.")
        self.channel_ranges[channel], range_converted = self._convert_input_range(_range)

        assert AlazarInputControl(
            self.handle,
            channel,
            DC_COUPLING,
            range_converted,
            IMPEDANCE_50_OHM
        ) == ApiSuccess

    @log_invoke_evt
    def set_repeats(self, repeats, current=None):
        self.repeats = self.align_repeats(repeats)

    @log_invoke_evt
    def set_trigger_level(self, trigger_level, current=None):
        self.trigger_level = trigger_level

        # convert relative level to U8
        trigger_level_volts = trigger_level
        trigger_range_volts = 5.0
        triggerLevel_code = U32(int(128 + 127 * (trigger_level_volts / trigger_range_volts)))
        assert AlazarSetTriggerOperation(
            self.handle, TRIG_ENGINE_OP_J, TRIG_ENGINE_J, TRIG_EXTERNAL, TRIGGER_SLOPE_POSITIVE, triggerLevel_code,
            TRIG_ENGINE_K, TRIG_DISABLE, TRIGGER_SLOPE_POSITIVE, U32(128)) == ApiSuccess

    @log_invoke_evt
    def set_trigger_delay(self, delay, current=None):
        self.trigger_delay = delay
        delay *= self.sample_rate  # timeout in unit of sample clocke

        assert AlazarSetTriggerDelay(self.handle, int(delay)) == ApiSuccess

    @log_invoke_evt
    def set_trigger_timeout(self, timeout, current=None):
        self.trigger_timeout = timeout
        timeout *= self.sample_rate  # timeout in unit of sample clock

        assert AlazarSetTriggerTimeOut(self.handle, int(timeout)) == ApiSuccess

    def get_sample_rate(self, current=None):
        return self.sample_rate

    def get_sample_number(self, current=None):
        return self.samples_per_records

    def get_input_range(self, channel, current=None):
        if channel not in [0, 1]:
            raise WrongParameterException(
                "There are only two channels: channel 0 and channel 1.")
        return self.channel_ranges[channel]

    def get_repeats(self, current=None):
        assert self.repeats > 0
        return self.repeats

    def get_trigger_level(self, current=None):
        return self.trigger_level

    def get_trigger_delay(self, current=None):
        return self.trigger_delay

    def get_trigger_timeout(self, current=None):
        return self.trigger_timeout

    @log_invoke_evt
    def acquire_and_fetch(self, current=None):
        self.start_acquire()
        return self.fetch()

    @log_invoke_evt
    def acquire_and_fetch_average(self, current=None):
        self.start_acquire()
        return self.fetch_average()

    @log_invoke_evt
    def start_acquire(self, current=None):
        assert AlazarSetRecordSize(
            self.handle,
            0,  # Pre-trigger
            self.samples_per_record  # Using two channels
        ) == ApiSuccess

        assert AlazarBeforeAsyncRead(
            self.handle,
            CHANNEL_A | CHANNEL_B,
            0,  # transfer offset
            self.samples_per_record,
            self.records_per_buffer,
            2 * self.repeats,
            ADMA_ALLOC_BUFFERS | ADMA_NPT | ADMA_EXTERNAL_STARTCAPTURE | ADMA_INTERLEAVE_SAMPLES
        ) == ApiSuccess

        assert AlazarStartCapture(
            self.handle
        ) == ApiSuccess

    def _fetch_data(self):
        assert self.repeats % self.records_per_buffer == 0
        records_per_buffer_each_channel = int(self.records_per_buffer / 2)
        num_of_buffers = int(self.repeats / records_per_buffer_each_channel)

        a_data = np.zeros([self.repeats, self.samples_per_record], dtype=np.uint8)
        b_data = np.zeros([self.repeats, self.samples_per_record], dtype=np.uint8)

        interleaved_record_length = self.samples_per_record * 2
        interleaved_samples_per_buffer = self.records_per_buffer * self.samples_per_record
        bytes_per_buffer = interleaved_samples_per_buffer  # Samples are in U8 format, == 1 byte each

        _buffer = (U8 * interleaved_samples_per_buffer)()  # U8 == 1 byte

        for n in range(num_of_buffers):
            ret_val = AlazarWaitNextAsyncBufferComplete(
                self.handle,
                _buffer,
                bytes_per_buffer,
                c_ulong(self.read_timeout * 1000)
            )

            assert ret_val == ApiSuccess or (n == num_of_buffers - 1 and ret_val == ApiTransferComplete)

            for i in range(records_per_buffer_each_channel):
                buffer_offset = i * interleaved_record_length
                record_window = _buffer[buffer_offset:buffer_offset + interleaved_record_length]
                a_data[n*records_per_buffer_each_channel+i] = record_window[0::2]
                b_data[n*records_per_buffer_each_channel+i] = record_window[1::2]

        assert AlazarAbortAsyncRead(self.handle) == ApiSuccess
        return a_data, b_data

    @log_invoke_evt
    def fetch(self, current=None):
        a_data, b_data = self._fetch_data()

        datasets = [pack_data_set(a_data), pack_data_set(b_data)]
        return datasets

    @log_invoke_evt
    def fetch_average(self, current=None):
        a_data, b_data = self._fetch_data()
        a_data_avg = a_data.mean(axis=0)
        b_data_avg = b_data.mean(axis=0)

        datasets = [pack_data_set(a_data_avg), pack_data_set(b_data_avg)]
        return datasets

    @staticmethod
    def align_samples_per_record(num_of_points):
        samples_per_record = (num_of_points // 64) * 64
        if samples_per_record < num_of_points:
            samples_per_record += 64
        return samples_per_record

    def align_repeats(self, repeats):
        if repeats % self.records_per_buffer != 0:
            repeats = (repeats // self.records_per_buffer + 1) * self.records_per_buffer
        return repeats

    @staticmethod
    def _parse_addr(addr):
        ats_addr = re.compile(
            r'^ATS(9360|9850|9870)::SYSTEM([0-9]+)::([0-9]+)(|::INSTR)$')
        # example: ATS9870::SYSTEM1::1
        m = ats_addr.search(addr)
        if m is None:
            raise WrongParameterException('ATS address error!')
        model = 'ATS' + str(m.group(1))  # ATS 9360|9850|9870
        system_id = int(m.group(2))
        board_id = int(m.group(3))
        return dict(model=model,
                    systemID=system_id,
                    boardID=board_id)

    def _convert_input_range(self, range_to_convert):
        input_conversion_table = {
            INPUT_RANGE_PM_20_MV: 0.02,
            INPUT_RANGE_PM_40_MV: 0.04,
            INPUT_RANGE_PM_50_MV: 0.05,
            INPUT_RANGE_PM_80_MV: 0.08,
            INPUT_RANGE_PM_100_MV: 0.1,
            INPUT_RANGE_PM_200_MV: 0.2,
            INPUT_RANGE_PM_400_MV: 0.4,
            INPUT_RANGE_PM_500_MV: 0.5,
            INPUT_RANGE_PM_800_MV: 0.8,
            INPUT_RANGE_PM_1_V: 1.0,
            INPUT_RANGE_PM_2_V: 2.0,
            INPUT_RANGE_PM_4_V: 4.0,
            INPUT_RANGE_PM_5_V: 5.0,
            INPUT_RANGE_PM_8_V: 8.0,
            INPUT_RANGE_PM_10_V: 10.0,
            INPUT_RANGE_PM_20_V: 20.0,
            INPUT_RANGE_PM_40_V: 40.0,
            INPUT_RANGE_PM_16_V: 16.0,
            INPUT_RANGE_PM_1_V_25: 1.25,
            INPUT_RANGE_PM_2_V_5: 2.5,
            INPUT_RANGE_PM_125_MV: 0.125,
            INPUT_RANGE_PM_250_MV: 0.25
        }

        if self.model in [ATS9325, ATS9350, ATS9850, ATS9870]:
            available = [
                INPUT_RANGE_PM_40_MV, INPUT_RANGE_PM_100_MV, INPUT_RANGE_PM_200_MV,
                INPUT_RANGE_PM_400_MV, INPUT_RANGE_PM_1_V, INPUT_RANGE_PM_2_V,
                INPUT_RANGE_PM_4_V
            ]
        elif self.model in [ATS9351, ATS9360]:
            available = [INPUT_RANGE_PM_400_MV]
        else:
            raise DeviceException("Unknown ATS model.")

        for option in available:
            if input_conversion_table[option] > range_to_convert:
                return input_conversion_table[option], option

        return input_conversion_table[available[-1]], available[-1]


def get_parser():
    parser = get_rack_argv_parser("Start the Alazar Digitizer rack.")

    parser.add_argument("name_address", nargs="+", type=str,
                        help="name and address of the PSG, in the format of "
                             "{name}@{address} (multiple instances can be loaded)."
                             "Address format: ^ATS(9360|9850|9870)::SYSTEM([0-9]+)::([0-9]+)(|::INSTR)$")
    return parser


def load_dev(rack, args=None, logger=None):
    name_address_pairs = []

    for name_addr in args.name_address:
        splited = name_addr.split("@")
        if len(splited) != 2:
            parser.print_help()
        name_address_pairs.append((splited[0], splited[1]))

    for name, addr in name_address_pairs:
        identifier = f"ATS_{name}"

        if logger:
            logger.info(f"Initializing {identifier} at {addr}...")

        ats = Alazar(name, addr)
        rack.load_device(identifier, ats)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    logger = get_logger()
    rack = DeviceRack("ATSRack", args.host, args.port, logger)

    load_dev(rack, args, logger)

    rack.start()
