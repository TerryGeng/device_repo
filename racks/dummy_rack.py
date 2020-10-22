from device_repo import DeviceRack, DummyDeviceTemplate, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser


class DummyDev(DummyDeviceTemplate):
    def __init__(self, data):
        self.data = data

    def get_type(self, current=None):
        return DeviceType.Dummy

    def get_data(self, current=None):
        return self.data


def start_dummy_rack(host, port, start_immediately=True):
    logger = get_logger()
    rack = DeviceRack("DummyRack", host, port, logger)

    dummy01 = DummyDev(b"Dummy data 1")
    dummy02 = DummyDev(b"Dummy data 2")
    dummy03 = DummyDev(b"Dummy data 3")

    rack.load_device("Dummy01", dummy01)
    rack.load_device("Dummy02", dummy02)
    rack.load_device("Dummy03", dummy03)

    if start_immediately:
        rack.start()
    return rack


if __name__ == "__main__":
    parser = get_rack_argv_parser("Start dummy rack for testing.")
    args = parser.parse_args()

    start_dummy_rack(args.host, args.port)

