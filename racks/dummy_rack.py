from driver.dummy import DummyDev
from device_repo import DeviceRack
from device_repo.utils import get_logger, get_rack_argv_parser


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

