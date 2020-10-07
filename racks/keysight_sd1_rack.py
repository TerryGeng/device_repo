import logging
import Ice
import numpy as np
from functools import wraps

from device_repo import AWGTemplate, DeviceRack, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser
from driver.keysight_sd1 import (
    SD_AOU, SD_Wave, SD_Waveshapes, SD_TriggerExternalSources,
    SD_TriggerBehaviors, SD_WaveformTypes, SD_TriggerModes)


def log_invoke_evt(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if isinstance(args[-1], Ice.Current):
            current = args[-1]
            args_str = str(args[1:-1])
            logging.info(f"{f.__name__} invoked by {current.con}, with"
                         f"parameters {args_str}")

        f(*args, **kwargs)
        return wrapper


class Keysight_M3202A(AWGTemplate):
    def __init__(self, chassis, slot, sample_rate=1e9):
        self.name = f"AWG M3202A Chassis{chassis} Slot{slot}"
        self.sample_rate = sample_rate
        self.dev = SD_AOU()
        self.chassis = chassis
        self.slot = slot

        self.dev.openWithSlot("M3202A", chassis, slot)
        self.dev.waveformFlush()
        for ch in [1, 2, 3, 4]:
            # make all channels work in AWG mode
            self.dev.channelWaveShape(ch, SD_Waveshapes.AOU_AWG)
            self.dev.channelAmplitude(ch, 1.0)
            self.dev.channelOffset(ch, 0.0)

            self.dev.AWGtriggerExternalConfig(ch,
                                              SD_TriggerExternalSources.
                                              TRIGGER_EXTERN,
                                              SD_TriggerBehaviors.TRIGGER_RISE)
            self.dev.AWGqueueConfig(ch, 1)  # Set queue mode to Cyclic(1)

    def get_type(self, current=None):
        return DeviceType.ArbitaryWaveformGenerator

    @log_invoke_evt
    def write_raw_waveform(self, channel, amplitude, raw_waveform,
                           current=None):
        """ICE method"""
        sd_wave = SD_Wave()

        # Bug / feature of M3020A.
        # 16 zeros have to be appended to mark as the end of the waveform.
        wave_data = np.concatenate((raw_waveform, np.zeros(16)))

        sd_wave.newFromArrayDouble(SD_WaveformTypes.WAVE_ANALOG, wave_data)
        self.dev.waveformLoad(sd_wave, waveformNumber=channel)
        self.dev.channelAmplitude(channel, amplitude)
        self.dev.AWGqueueWaveform(channel,
                                  waveformNumber=channel,
                                  triggerMode=SD_TriggerModes.EXTTRIG,
                                  startDelay=0,
                                  cycles=1,
                                  prescaler=0)

    @log_invoke_evt
    def set_channel_offset(self, channel, offset_voltage, current=None):
        """ICE method"""
        self.dev.channelOffset(channel, offset_voltage)

    @log_invoke_evt
    def run_all(self, current=None):
        """ICE method"""
        for ch in [1, 2, 3, 4]:
            self.dev.AWGstart(ch)

    @log_invoke_evt
    def run_channel(self, channel, current=None):
        """ICE method"""
        self.dev.AWGstart(channel)

    @log_invoke_evt
    def stop_all(self, current=None):
        """ICE method"""

        for ch in [1, 2, 3, 4]:
            self.dev.AWGstop(ch)
            self.dev.AWGflush(ch)

    @log_invoke_evt
    def stop_channel(self, channel, current=None):
        """ICE method"""
        self.dev.AWGstop(channel)
        self.dev.AWGflush(channel)

    @log_invoke_evt
    def set_channel_amplitude(self, ch, amp, current=None):
        """ICE method"""
        self.dev.channelAmplitude(ch, amp)


def host_start(bind_address, bind_port, devs):
    with Ice.initialize([]) as ic:
        logging.info(f"Starting host at {bind_address}:{bind_port}...")
        adapter = ic.createObjectAdaperWithEndpoints(
            "KeysightSD1",
            f"tcp -h {bind_address} -p {bind_port}")

        for dev in devs:
            chasis, slot = dev
            identifier = f"KeysightM3202A_C{chasis}_S{slot}"

            logging.info(f"Initializing {identifier}...")
            keysight = Keysight_M3202A(chasis, slot)

            adapter.add(keysight, ic.stringToIdentity(identifier))

        adapter.activate()
        logging.info("Host activated. Waiting for incoming connections.")

        try:
            ic.waitForShutdown()
        except KeyboardInterrupt:
            pass


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
        identifier = f"KeysightM3202A_C{chasis}_S{slot}"

        logging.info(f"Initializing {identifier}...")
        keysight = Keysight_M3202A(chasis, slot)

        rack.load_device(identifier, keysight)

    rack.start()
