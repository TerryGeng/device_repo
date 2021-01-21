from device_repo import DCSourceTemplate, DeviceRack, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser, log_invoke_evt

if __name__ == "__main__":
    from driver.visa_device import VisaDeviceBase, get_device_by_address
else:
    from racks.driver.visa_device import VisaDeviceBase, get_device_by_address

import pyvisa


class DCSourceChannel(DCSourceTemplate, VisaDeviceBase):
    def __init__(self, name, ch, dev):
        super().__init__(dev)
        self.name = f"{name}_Ch{ch}"
        self.ch = ch

    def get_type(self, current=None):
        return DeviceType.DCSource

    @log_invoke_evt
    def set_offset(self, voltage_in_volts, current=None):
        self.visa_write(f':SNDT {self.ch}, "VOLT {voltage_in_volts:.3f}"')

    @log_invoke_evt
    def get_offset(self, current=None):
        return float(
            self.visa_query(f':SNDT {self.ch}, "VOLT?"')
        )

    @log_invoke_evt
    def output_on(self, current=None):
        """ICE method"""
        self.visa_write(f':SNDT {self.ch}, "OPON"')

    @log_invoke_evt
    def output_off(self, current=None):
        """ICE method"""
        self.visa_write(f':SNDT {self.ch}, "OPOF"')


def get_parser():
    parser = get_rack_argv_parser("Start the SRS DC source rack.")

    parser.add_argument("--address", type=str, dest="address",
                        help="VISA address of the SRS")
    parser.add_argument("--name", type=str, dest="name", default="",
                        help="name of the SRS")
    return parser


def load_dev(rack, args, logger=None):
    name = args.name

    logger.info(f"Open resource at {args.address}...")
    dev = get_device_by_address(args.address)

    for ch in [1, 2, 3, 4, 5, 6, 7, 8]:
        _id = f"{name}_CH{ch}"

        srs = DCSourceChannel(_id, ch, dev)
        rack.load_device(name, srs)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    logger = get_logger()
    rack = DeviceRack("DC_SRSRack", args.host, args.port, logger)

    load_dev(rack, args, logger)

    rack.start()
