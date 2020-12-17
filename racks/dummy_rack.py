from device_repo import DeviceRack, DummyDeviceTemplate, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser, InvalidParameterException


class DummyDev(DummyDeviceTemplate):
    def __init__(self, data):
        self.data = data

    def get_type(self, current=None):
        return DeviceType.Dummy

    def get_data(self, current=None):
        return self.data


def get_parser():
    parser = get_rack_argv_parser("Start dummy rack for testing.")

    parser.add_argument("name_data", nargs="+", type=str,
                        help="name and dummy data of the dummy device, in the format of "
                             "{name}:{data} (multiple instances can be loaded)")
    return parser


def start_dummy_rack(host, port, start_immediately=True, args=None):
    logger = get_logger()
    rack = DeviceRack("DummyRack", host, port, logger)

    load_dev(rack, args, logger)

    if start_immediately:
        rack.start()
    return rack


def load_dev(rack, args=None, logger=None):
    import re
    for name_data in args.name_data:
        splited = re.match("(.+):(.+)", name_data)

        if not splited:
            raise InvalidParameterException

        dummy = DummyDev(splited[2].encode("utf-8") if args else b"Dummy data 1")
        rack.load_device(splited[1], dummy)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    start_dummy_rack(args.host, args.port, True, args)

