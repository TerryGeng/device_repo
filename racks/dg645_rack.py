from device_repo import DGTemplate, DeviceRack, DeviceType, WrongParameterException
from device_repo.utils import (get_logger, get_rack_argv_parser, log_invoke_evt,
                               InvalidParameterException)

if __name__ == "__main__":
    from driver.visa_device import VisaDeviceBase, get_device_by_address
else:
    from .driver.visa_device import VisaDeviceBase, get_device_by_address


class DG645(DGTemplate, VisaDeviceBase):
    def __init__(self, id, dev):
        super().__init__(dev)
        self.id = id

        self.visa_write("TSRC 0")  # Use Internal Trigger

    def get_type(self, current=None):
        return DeviceType.DelayGenerator

    @log_invoke_evt
    def set_cycle_frequency(self, freq_in_hz, current=None):
        self.visa_write(f"TRAT {freq_in_hz:.6f} Hz")

    @log_invoke_evt
    def get_cycle_frequency(self, current=None):
        return float(self.visa_query(f"TRAT?"))

    @log_invoke_evt
    def set_channel_delay(self, channel_index, rising_at, fall_after, current=None):
        if channel_index not in [0, 1, 2, 3, 4]:
            raise WrongParameterException("channel_index out of range. "
                                          "There are only 0(T0), 1(AB), 2(CD), 3(EF), "
                                          "4(GH) on this device.")
        if channel_index != 0:
            self.visa_write(f"DLAY {2*channel_index},0,{rising_at:.12f}")
        else:
            if rising_at != 0:
                raise WrongParameterException("The rising edge of channel 0(T0) "
                                              "is not settable, which is always 0.")
        self.visa_write(f"DLAY {2*channel_index+1},{2*channel_index},{fall_after:.12f}")

    @log_invoke_evt
    def get_channel_delay(self, channel_index, current=None):
        if channel_index not in [0, 1, 2, 3, 4]:
            raise WrongParameterException("channel_index out of range. "
                                          "There are only 0(T0), 1(AB), 2(CD), 3(EF), "
                                          "4(GH) on this device.")

        ch1, rising_edge = self._parse_edge(self.visa_query(f"DLAY?{2*channel_index}"))
        assert ch1 == 0
        ch2, falling_edge = self._parse_edge(self.visa_query(f"DLAY?{2*channel_index+1}"))
        assert ch2 == 2*channel_index
        return rising_edge, falling_edge

    def _parse_edge(self, query_result):
        split = query_result.split(",")
        related_to_channel, time = int(split[0]), float(split[1])
        return related_to_channel, time


def get_parser():
    parser = get_rack_argv_parser("Start the DG645 rack.")

    parser.add_argument("name_address", nargs="+", type=str,
                        help="name and VISA address of the DG645, in the format of "
                             "{name}@{address} (multiple instances can be loaded)")
    return parser


def load_dev(rack, args=None, logger=None):
    name_address_pairs = []

    for name_addr in args.name_address:
        splited = name_addr.split("@")
        if len(splited) != 2:
            raise InvalidParameterException
        name_address_pairs.append((splited[0], splited[1]))

    for name, addr in name_address_pairs:
        dev = get_device_by_address(addr)
        identifier = f"DG645_{name}"

        if logger:
            logger.info(f"Initializing {identifier} at {addr}...")

        dg = DG645(identifier, dev)
        rack.load_device(identifier, dg)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    logger = get_logger()
    rack = DeviceRack("DG645Rack", args.host, args.port, logger)

    try:
        load_dev(rack, args, logger)
    except InvalidParameterException:
        parser.print_help()
        exit(1)

    rack.start()
