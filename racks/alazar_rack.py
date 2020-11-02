from device_repo.utils import get_logger, get_rack_argv_parser, log_invoke_evt
from device_repo import (DigitizerTemplate, DeviceException, WrongParameterException,
                         DoubleDataSet, DeviceType, DeviceRack)
import logging
import time

import numpy as np
import re

from racks.driver.alazar import alazar_wrapper
from racks.driver.alazar import alazar_api
from racks.driver.alazar.alazar_wrapper import (AlazarTechDigitizer, AutoDMA, DMABufferArray)


class Alazar(DigitizerTemplate):
    def __init__(self, name, addr, *,
                 sample_per_records=1024,
                 repeats=512,
                 channel_ranges=(0, 0),
                 trigger_level=0.0,
                 trigger_delay=0.0,
                 trigger_timeout=0.0,
                 records_per_buffer=64,
                 buffer_count=512):
        super().__init__()

        self.name = name
        self.addr = addr
        dict_parse = self._parse_addr(self.addr)

        self.model = dict_parse.get('model', None)
        self.system_id = dict_parse.get('systemID', 1)
        self.board_id = dict_parse.get('boardID', 1)
        self.handle = AlazarTechDigitizer(self.system_id, self.board_id)

        self.sample_per_records = self.align_samples_per_record(sample_per_records)
        self.records_per_buffer = records_per_buffer
        self.repeats = repeats
        self.trigger_level = trigger_level
        self.trigger_delay = trigger_delay
        self.trigger_timeout = trigger_timeout
        self.buffer_count = buffer_count

        self.channel_ranges = channel_ranges

        # self.config['e'] = self.get_exp_array(
        #     self.config['fft_freq_list'], self.config['n'],
        #     self.config['weight'],
        #     self.config['sampleRate']
        # )

        self.initialize()
        self.configure()

    def initialize(self):
        self.handle.setCaptureClock(alazar_api.EXTERNAL_CLOCK_10MHz_REF, alazar_api.SAMPLE_RATE_1GSPS)
        self.handle.setBWLimit(alazar_api.CHANNEL_A, 0)
        self.handle.setBWLimit(alazar_api.CHANNEL_B, 0)
        self.handle.setExternalTrigger(alazar_api.DC_COUPLING)
        self.handle.configureAuxIO(alazar_api.AUX_OUT_TRIGGER, 0)
        self.handle.setParameter(0, alazar_api.SET_DATA_FORMAT, alazar_api.DATA_FORMAT_UNSIGNED)

    def configure(self):
        self.handle.inputControl(alazar_api.CHANNEL_A, alazar_api.DC_COUPLING,
                                 alazar_wrapper.getInputRange(self.channel_ranges[0], self.handle.kind),
                                 alazar_api.IMPEDANCE_50_OHM)
        self.handle.inputControl(alazar_api.CHANNEL_B, alazar_api.DC_COUPLING,
                                 alazar_wrapper.getInputRange(self.channel_ranges[1], self.handle.kind),
                                 alazar_api.IMPEDANCE_50_OHM)

        # convert relative level to U8
        maxLevel = 5.0
        Level = int(128 + 127 * self.trigger_level / maxLevel)
        JLevel = Level
        KLevel = Level
        self.handle.setTriggerOperation(
            alazar_api.TRIG_ENGINE_OP_J, alazar_api.TRIG_ENGINE_J, alazar_api.TRIG_EXTERNAL,
            alazar_api.TRIGGER_SLOPE_POSITIVE, JLevel, alazar_api.TRIG_ENGINE_K,
            alazar_api.TRIG_DISABLE, alazar_api.TRIGGER_SLOPE_POSITIVE, KLevel)

        self.handle.setTriggerDelay(self.trigger_delay)
        self.handle.setTriggerTimeOut(self.trigger_timeout)

        self.handle.setParameter(0, alazar_api.SETGET_ASYNC_BUFFCOUNT, self.buffer_count)

    def get_type(self, current=None):
        return DeviceType.Digitizer

    @log_invoke_evt
    def set_sample_number(self, number_of_samples, current=None):
        self.sample_per_records = self.align_samples_per_record(number_of_samples)

    @log_invoke_evt
    def set_input_range(self, channel, _range, current=None):
        if channel not in [0, 1]:
            raise WrongParameterException(
                "There are only two channels: channel 0 and channel 1.")
        self.channel_ranges[channel] = _range
        self.configure()

    @log_invoke_evt
    def set_repeats(self, repeats, current=None):
        self.repeats = self.align_repeats(repeats)

    @log_invoke_evt
    def set_trigger_level(self, trigger_level, current=None):
        self.trigger_level = trigger_level
        self.configure()

    @log_invoke_evt
    def set_trigger_delay(self, delay, current=None):
        self.trigger_delay = delay
        self.configure()

    @log_invoke_evt
    def set_trigger_timeout(self, timeout, current=None):
        self.trigger_timeout = timeout
        self.configure()

    def get_sample_rate(self, current=None):
        return 1e9

    def get_sample_number(self, current=None):
        return self.get_sample_number()

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

    def _get_buffer_count(self, buffer_count):
        self.buffer_count = buffer_count
        self.configure()

    @log_invoke_evt
    def acquire(self, current=None):
        a_data, b_data = self.get_data()
        datasets = [
            DoubleDataSet(
                shape=a_data.shape,
                array=a_data.flatten()
            ),
            DoubleDataSet(
                shape=b_data.shape,
                array=b_data.flatten()
            )
        ]
        return datasets

    def _acquire_data(self, samples_per_record, repeats, buffers, records_per_buffer,
                      timeout):
        with AutoDMA(self.handle,
                     samples_per_record,
                     repeats=repeats,
                     buffers=buffers,
                     recordsPerBuffer=records_per_buffer,
                     timeout=timeout) as h:
            yield from h.read()

    def get_data(self, avg=False):
        samples_per_record = self.sample_per_records
        records_per_buffer = self.records_per_buffer
        repeats = self.repeats
        e = self.config['e']
        n = e.shape[0]

        a = np.zeros([repeats, records_per_buffer*samples_per_record])
        b = np.zeros([repeats, records_per_buffer*samples_per_record])

        retry = 0  # What this this?
        n = 0

        for chA, chB in self._acquire_data(
                samples_per_record,
                repeats=repeats,
                buffers=None,
                records_per_buffer=records_per_buffer,
                timeout=1):

            n += records_per_buffer

            a_lst = chA.reshape((records_per_buffer, samples_per_record))
            b_lst = chB.reshape((records_per_buffer, samples_per_record))

            a[n:records_per_buffer] = a_lst
            b[n:records_per_buffer] = b_lst

            if repeats == 0:
                break
        if avg:
            return a.mean(axis=0), b.mean(axis=0)
        else:
            return a, b

        # while retry < 3:
        #     try:
        #         for chA, chB in self._acquire_data(
        #                 samples_per_record,
        #                 repeats=repeats,
        #                 buffers=None,
        #                 records_per_buffer=records_per_buffer,
        #                 timeout=1):
        #             A_lst = chA.reshape((records_per_buffer, samples_per_record))
        #             B_lst = chB.reshape((records_per_buffer, samples_per_record))
        #             if fft:
        #                 A_lst = (A_lst[:, :n]).dot(e) / n
        #                 B_lst = (B_lst[:, :n]).dot(e) / n
        #             try:
        #                 A = np.r_[A, A_lst]
        #                 B = np.r_[B, B_lst]
        #             except:
        #                 A, B = A_lst, B_lst
        #             if repeats == 0 and A.shape[1] >= maxlen:
        #                 break
        #         if avg:
        #             return A.mean(axis=0), B.mean(axis=0)
        #         else:
        #             return A, B
        #     except AlazarTechError as err:
        #         log.exception(err.msg)
        #         if err.code == 518:
        #             raise SystemExit(2)
        #         else:
        #             pass
        #     time.sleep(0.1)
        #     retry += 1
        # else:
        #     raise SystemExit(1)

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

    # @staticmethod
    # def get_exp_array(fft_freq_list, numOfPoints, weight=None, sampleRate=1e9):
    #     e = []
    #     t = np.arange(0, numOfPoints, 1) / sampleRate
    #     if weight is None:
    #         weight = np.ones(numOfPoints)
    #     for f in fft_freq_list:
    #         e.append(weight * np.exp(-1j * 2 * np.pi * f * t))
    #     return np.asarray(e).T

    @staticmethod
    def _parse_addr(addr):
        ats_addr = re.compile(
            r'^ATS(9360|9850|9870)::SYSTEM([0-9]+)::([0-9]+)(|::INSTR)$')
        # example: ATS9870::SYSTEM1::1
        m = ats_addr.search(addr)
        if m is None:
            raise WrongParameterException('ATS address error!')
        model = 'ATS'+str(m.group(1))  # ATS 9360|9850|9870
        system_id = int(m.group(2))
        board_id = int(m.group(3))
        return dict(model=model,
                    systemID=system_id,
                    boardID=board_id)


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

        psg = Alazar(name, addr)
        rack.load_device(identifier, psg)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    logger = get_logger()
    rack = DeviceRack("ATSRack", args.host, args.port, logger)

    load_dev(rack, args, logger)

    rack.start()
