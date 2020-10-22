from device_repo import DCSourceTemplate, DeviceRack, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser, log_invoke_evt

import pyvisa


class DCSource:
    def __init__(self, address):
        self.resource_mgr = pyvisa.ResourceManager()
        self.dev = self.resource_mgr.open_resource(address)


class DCSourceChannel(DCSourceTemplate):
    def __init__(self, name, ch, dev):
        self.name = f"DC_SRS_{name}_Ch{ch}"
        self.ch = ch
        self.dev = dev

    def get_type(self, current=None):
        return DeviceType.DCSource

    @log_invoke_evt
    def set_offset(self, voltage_in_volts, current=None):
        self.dev.write(f':SNDT {self.ch}, "VOLT {voltage_in_volts:.3f}"')

    @log_invoke_evt
    def get_offset(self, current=None):
        return float(
            self.dev.write(f':SNDT {self.ch}, "VOLT?"')
        )

    @log_invoke_evt
    def output_on(self, current=None):
        """ICE method"""
        self.dev.write(f':SNDT {self.ch}, "OPON"')

    @log_invoke_evt
    def output_off(self, current=None):
        """ICE method"""
        self.dev.write(f':SNDT {self.ch}, "OPOF"')


if __name__ == "__main__":
    parser = get_rack_argv_parser("Start the SRS DC source rack.")

    parser.add_argument("--address", type=str, dest="address",
                        help="VISA address of the SRS")
    parser.add_argument("--name", type=str, dest="name",
                        help="name of the SRS")
    args = parser.parse_args()

    logger = get_logger()
    name = args.name
    resource_mgr = pyvisa.ResourceManager()
    ch_dict = {}
    rack = DeviceRack("DC_SRSRack", args.host, args.port, logger)

    logger.info(f"Open resource at {args.address}...")
    dev = resource_mgr.open_resource(args.address)

    for ch in [1, 2, 3, 4, 5, 6, 7, 8]:
        identifier = f"DC_SRS_{name}_{ch}"

        srs = DCSourceChannel(identifier, ch, dev)
        rack.load_device(identifier, srs)

    rack.start()
