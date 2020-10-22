from device_repo import PSGTemplate, DeviceRack, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser, log_invoke_evt

import pyvisa


class PSG(PSGTemplate):
    def __init__(self, name, address):
        self.name = f"PSG {name} @ {address}"
        self.address = address
        self.resource_mgr = pyvisa.ResourceManager()
        self.dev = self.resource_mgr.open_resource(address)

    def get_type(self, current=None):
        return DeviceType.ParametricSignalGenerator

    @log_invoke_evt
    def set_frequency(self, freq_in_hz, current=None):
        self.dev.write(f":FREQ {freq_in_hz:.13e} Hz")

    @log_invoke_evt
    def get_frequency(self, current=None):
        return float(self.dev.query(f":FREQ?"))

    @log_invoke_evt
    def set_power(self, amp_in_dbm, current=None):
        """ICE method"""
        self.dev.write(f":POWER {amp_in_dbm:.8e} dBm")

    @log_invoke_evt
    def get_power(self, current=None):
        return float(self.dev.query(f":POWER?"))

    @log_invoke_evt
    def run(self, current=None):
        """ICE method"""
        self.dev.write(":OUTP ON")

    @log_invoke_evt
    def stop(self, current=None):
        """ICE method"""
        self.dev.write(":OUTP OFF")


if __name__ == "__main__":
    parser = get_rack_argv_parser("Start the general PSG rack.")

    parser.add_argument("name_address", nargs="+", type=str,
                        help="name and VISA address of the PSG, in the format of "
                             "{name}@{address} (multiple instances can be loaded)")
    args = parser.parse_args()

    name_address_pairs = []

    for name_addr in args.name_address:
        splited = name_addr.split("@")
        if len(splited) != 2:
            parser.print_help()
        name_address_pairs.append((splited[0], splited[1]))

    logger = get_logger()
    rack = DeviceRack("PSGRack", args.host, args.port, logger)

    for name, addr in name_address_pairs:
        identifier = f"PSG_{name}"
        logger.info(f"Initializing {identifier} at {addr}...")

        psg = PSG(name, addr)
        rack.load_device(identifier, psg)

    rack.start()
