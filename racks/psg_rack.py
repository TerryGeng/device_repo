from device_repo import PSGTemplate, DeviceRack, DeviceType
from device_repo.utils import (get_logger, get_rack_argv_parser, log_invoke_evt,
                               InvalidParameterException)

if __name__ == "__main__":
    from driver.visa_device import VisaDeviceBase, get_device_by_address
else:
    from racks.driver.visa_device import VisaDeviceBase, get_device_by_address


class PSG(PSGTemplate, VisaDeviceBase):
    def __init__(self, id, dev):
        super().__init__(dev)
        self.id = id

    def get_type(self, current=None):
        return DeviceType.ParametricSignalGenerator

    @log_invoke_evt
    def set_frequency(self, freq_in_hz, current=None):
        self.visa_write(f":FREQ {freq_in_hz:.13e} Hz")

    @log_invoke_evt
    def get_frequency(self, current=None):
        return float(self.visa_query(f":FREQ?"))

    @log_invoke_evt
    def set_power(self, amp_in_dbm, current=None):
        """ICE method"""
        self.visa_write(f":POWER {amp_in_dbm:.8e} dBm")

    @log_invoke_evt
    def get_power(self, current=None):
        return float(self.visa_query(f":POWER?"))

    @log_invoke_evt
    def run(self, current=None):
        """ICE method"""
        self.visa_write(":OUTP ON")

    @log_invoke_evt
    def stop(self, current=None):
        """ICE method"""
        self.visa_write(":OUTP OFF")


def get_parser():
    parser = get_rack_argv_parser("Start the general PSG rack. Support: SRS series, "
                                  "Keysight series, etc.")

    parser.add_argument("name_address", nargs="+", type=str,
                        help="name and VISA address of the PSG, in the format of "
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

        if logger:
            logger.info(f"Initializing {name} at {addr}...")

        psg = PSG(name, dev)
        rack.load_device(name, psg)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    logger = get_logger()
    rack = DeviceRack("PSGRack", args.host, args.port, logger)

    try:
        load_dev(rack, args, logger)
    except InvalidParameterException:
        parser.print_help()
        exit(1)

    rack.start()
