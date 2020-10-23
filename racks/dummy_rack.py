from device_repo import DeviceRack, DummyDeviceTemplate, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser


class DummyDev(DummyDeviceTemplate):
    def __init__(self, data):
        self.data = data

    def get_type(self, current=None):
        return DeviceType.Dummy

    def get_data(self, current=None):
        return self.data


def get_parser():
    parser = get_rack_argv_parser("Start dummy rack for testing.")

    parser.add_argument("--data0", type=str, dest="data0", default="Dummy data 1",
                        help="data0")
    parser.add_argument("--data1", type=str, dest="data1", default="Dummy data 2",
                        help="data1")
    parser.add_argument("--data2", type=str, dest="data2", default="Dummy data 3",
                        help="data2")
    return parser


def start_dummy_rack(host, port, start_immediately=True, args=None):
    logger = get_logger()
    rack = DeviceRack("DummyRack", host, port, logger)

    load_dev(rack, args, logger)

    if start_immediately:
        rack.start()
    return rack


def load_dev(rack, args=None, logger=None):
    dummy01 = DummyDev(args.data0.encode("utf-8") if args else b"Dummy data 1")
    dummy02 = DummyDev(args.data1.encode("utf-8") if args else b"Dummy data 2")
    dummy03 = DummyDev(args.data2.encode("utf-8") if args else b"Dummy data 3")

    rack.load_device("Dummy01", dummy01)
    rack.load_device("Dummy02", dummy02)
    rack.load_device("Dummy03", dummy03)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    start_dummy_rack(args.host, args.port, True, args)

