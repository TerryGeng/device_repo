from device_repo import DeviceRack
from device_repo.utils import get_logger

from . import get_device_module


def start_rack_with_config(start_immediately=True):
    import argparse
    import yaml

    logger = get_logger()
    parser = argparse.ArgumentParser(
        description="Rack starter of the DeviceRepo.")

    parser.add_argument("-c", "--config", dest="config", type=str,
                        help="path to the config file")
    args = parser.parse_args()

    config = None
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    try:
        host_addr = config['network']['host_address']
        host_port = config['network']['host_port']
    except KeyError:
        print("Error: No host address or port discovered in the config file.")
        exit(1)

    try:
        dev_init_list = config['devices']
        assert isinstance(dev_init_list, list)
        assert len(dev_init_list) > 0
    except (KeyError, AssertionError):
        print("Error: No device initialization instruction discovered in the config file.")
        exit(1)

    device_module = get_device_module()
    rack = DeviceRack("RackStater", host_addr, host_port, logger)

    for dev_init_inst in dev_init_list:
        argv = list(filter(lambda x: x, dev_init_inst.split(" ")))
        dev = argv[0].lower()
        logger.info(f"=> Initializing device {argv[0]}")
        if dev in device_module:
            parser = device_module[dev].get_parser()
            try:
                argv.pop(0)
                args = parser.parse_args(argv)
            except SystemExit:
                print(f"Error: Invalid initialization instruction for {argv[0]}.")
                exit(1)

            device_module[dev].load_dev(rack, args, logger)
        else:
            print(f"Error: Device {argv[0]} not found.")
            exit(1)

    logger.info("Initialization finished.")

    if start_immediately:
        rack.start()
    return rack
