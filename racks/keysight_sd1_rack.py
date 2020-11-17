from device_repo import AWGTemplate, DeviceRack, DeviceType
from device_repo.utils import (get_logger, get_rack_argv_parser, log_invoke_evt,
                               InvalidParameterException)
import numpy as np

if __name__ != "__main__":
    from racks.driver.keysight_sd1 import (SD_AOU, SD_Waveshapes, SD_TriggerExternalSources,
                                      SD_TriggerBehaviors, SD_Wave, SD_WaveformTypes, SD_TriggerModes)
else:
    from driver.keysight_sd1 import (SD_AOU, SD_Waveshapes, SD_TriggerExternalSources,
                                     SD_TriggerBehaviors, SD_Wave, SD_WaveformTypes, SD_TriggerModes)


class Keysight_M3202A(AWGTemplate):
    def __init__(self, chassis, slot, channel):

        self.name = f"AWG M3202A Chassis{chassis} Slot{slot} Channel{channel}"
        self.sample_rate = 1e9
        self.dev = SD_AOU()
        self.chassis = chassis
        self.slot = slot
        self.channel = channel
        self.offset = 0.0
        self.amplitude = 1.0

        self.dev.openWithSlot("M3202A", chassis, slot)
        self.dev.channelWaveShape(channel, SD_Waveshapes.AOU_AWG)
        self.dev.channelAmplitude(channel, self.amplitude)
        self.dev.channelOffset(channel, self.offset)

        self.dev.AWGtriggerExternalConfig(channel,
                                          SD_TriggerExternalSources.
                                          TRIGGER_EXTERN,
                                          SD_TriggerBehaviors.TRIGGER_RISE)
        self.dev.AWGqueueConfig(channel, 1)  # Set queue mode to Cyclic(1)

    def get_type(self, current=None):
        return DeviceType.ArbitraryWaveformGenerator

    @log_invoke_evt
    def get_sample_rate(self):
        return self.sample_rate

    @log_invoke_evt
    def write_raw_waveform(self, raw_waveform, amplitude, current=None):
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
        self.offset = offset_voltage
        self.dev.channelOffset(self.channel, offset_voltage)

    @log_invoke_evt
    def get_offset(self, current=None):
        """ICE method"""
        return self.offset

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
        self.amplitude = amp
        self.dev.channelAmplitude(self.channel, amp)

    @log_invoke_evt
    def get_amplitude(self, current=None):
        """ICE method"""
        return self.amplitude


def get_parser():
    parser = get_rack_argv_parser("Start the Keysight M3202A rack.")

    parser.add_argument("location", nargs="+", type=str,
                        help="location of the M3202A, in the format of "
                             "{chasis}:{slot} (multiple instances can be loaded)")
    return parser


def load_keysight_m3202a(rack, chasis, slot, identifier="", logger=None):
    for channel in [1, 2, 3, 4]:
        _id = ""
        if not identifier:
            _id = f"M3202A_C{chasis}_S{slot}_CH{channel}"
        else:
            _id = identifier + f"_CH{channel}"
        if logger:
            logger.info(f"Initializing {_id}...")
        keysight = Keysight_M3202A(chasis, slot, channel)
        rack.load_device(_id, keysight)


def load_dev(rack, args=None, logger=None):
    awgs = []
    for location in args.location:
        splited = location.split(":")
        if len(splited) != 2 or not isinstance(splited[0], int) or \
                not isinstance(splited[1], int):
            raise InvalidParameterException
        awgs.append((int(splited[0]), int(splited[1])))

    for awg in awgs:
        chasis, slot = awg
        load_keysight_m3202a(rack, chasis, slot, "", logger)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    logger = get_logger()
    rack = DeviceRack("KeysightM3202ARack", args.host, args.port, logger)
    try:
        load_dev(rack, args, logger)
    except InvalidParameterException:
        parser.print_help()
        exit(1)

    rack.start()
