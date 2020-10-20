import logging
import Ice
import numpy as np

from device_repo import AWGTemplate, DeviceRack, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser, log_invoke_evt
from driver.keysight_sd1 import (
    SD_AOU, SD_Wave, SD_Waveshapes, SD_TriggerExternalSources,
    SD_TriggerBehaviors, SD_WaveformTypes, SD_TriggerModes)


class Keysight_M3202A(AWGTemplate):
    def __init__(self, chassis, slot, channel, sample_rate=1e9):
        self.name = f"AWG M3202A Chassis{chassis} Slot{slot} Channel{channel}"
        self.sample_rate = sample_rate
        self.dev = SD_AOU()
        self.chassis = chassis
        self.slot = slot
        self.channel = channel

        self.dev.openWithSlot("M3202A", chassis, slot)
        self.dev.waveformFlush()
        # make all channelannels work in AWG mode
        self.dev.channelWaveShape(channel, SD_Waveshapes.AOU_AWG)
        self.dev.channelAmplitude(channel, 1.0)
        self.dev.channelOffset(channel, 0.0)

        self.dev.AWGtriggerExternalConfig(channel,
                                          SD_TriggerExternalSources.
                                          TRIGGER_EXTERN,
                                          SD_TriggerBehaviors.TRIGGER_RISE)
        self.dev.AWGqueueConfig(channel, 1)  # Set queue mode to Cyclic(1)

    def get_type(self, current=None):
        return DeviceType.ArbitraryWaveformGenerator

    @log_invoke_evt
    def write_raw_waveform(self, amplitude, raw_waveform,
                           current=None):
        """ICE method"""
        sd_wave = SD_Wave()

        # Bug / feature of M3020A.
        # 16 zeros have to be appended to mark as the end of the waveform.
        wave_data = np.concatenate((raw_waveform, np.zeros(16)))

        sd_wave.newFromArrayDouble(SD_WaveformTypes.WAVE_ANALOG, wave_data)
        self.dev.waveformLoad(sd_wave, waveformNumber=self.channel)
        self.dev.channelAmplitude(self.channel, amplitude)
        self.dev.AWGqueueWaveform(self.channel,
                                  waveformNumber=self.channel,
                                  triggerMode=SD_TriggerModes.EXTTRIG,
                                  startDelay=0,
                                  cycles=1,
                                  prescaler=0)

    @log_invoke_evt
    def set_offset(self, offset_voltage, current=None):
        """ICE method"""
        self.dev.channelOffset(self.channel, offset_voltage)

    @log_invoke_evt
    def run(self, current=None):
        """ICE method"""
        self.dev.AWGstart(self.channel)

    @log_invoke_evt
    def stop(self, current=None):
        """ICE method"""
        self.dev.AWGstop(self.channel)
        self.dev.AWGflush(self.channel)

    @log_invoke_evt
    def set_amplitude(self, amp, current=None):
        """ICE method"""
        self.dev.channelAmplitude(self.channel, amp)


if __name__ == "__main__":
    parser = get_rack_argv_parser("Start the Keysight M3202A rack.")

    parser.add_argument("location", nargs="+", dest="location", type=str,
                        help="location of the M3202A, in the format of "
                        "{chasis}:{slot} (multiple instances can be loaded)")
    args = parser.parse_args()

    awgs = []

    for location in args.location:
        splited = location.split(":")
        if len(splited) != 2 or not isinstance(splited[0], int) or \
                not isinstance(splited[1], int):
            parser.print_help()
        awgs.append((int(splited[0]), int(splited[1])))

    logger = get_logger()
    rack = DeviceRack("KeysightM3202ARack", args.host, args.port, logger)

    for awg in awgs:
        chasis, slot = awg
        for channel in [1, 2, 3, 4]:
            identifier = f"KeysightM3202A_C{chasis}_S{slot}_CH_{channel}"
            logger.info(f"Initializing {identifier}...")
            keysight = Keysight_M3202A(chasis, slot, channel)
            rack.load_device(identifier, keysight)

    rack.start()
