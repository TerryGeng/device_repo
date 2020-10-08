from device_repo import DeviceRack, DummyDeviceTemplate, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser


class DummyDev(DummyDeviceTemplate):
    def __init__(self):
        pass

    def get_type(self, current=None):
        return DeviceType.Dummy

    def get_data(self, current=None):
        return b"Hello world!"


def start_dummy_rack(host, port, start_immediately=True):
    logger = get_logger()
    rack = DeviceRack("DummyRack", host, port, logger)
    dummy = DummyDev()
    rack.load_device("Dummy01", dummy)

    if start_immediately:
        rack.start()
    return rack


if __name__ == "__main__":
    parser = get_rack_argv_parser("Start dummy rack for testing.")
    args = parser.parse_args()

    start_dummy_rack(args.host, args.port)

