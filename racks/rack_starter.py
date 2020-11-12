import os
import sys
import pkgutil
import argparse
import yaml
import re

from importlib import import_module
from device_repo import DeviceRack
from device_repo.utils import get_logger, InvalidParameterException

# This module should be run with start_racks.py


def list_all_racks():
    # import all racks
    racks_dict = {}

    dirname = "racks"
    for module_info in pkgutil.iter_modules([dirname]):
        package_name = module_info.name
        match = re.match("(.*)_rack", package_name)
        if not match:
            continue

        rack_name = match[1]

        full_package_name = f"{dirname}.{package_name}"
        racks_dict[rack_name] = (full_package_name, module_info)

    return racks_dict


def get_module(full_package_name, module_info):
    if full_package_name not in sys.modules:
        module = module_info.find_module(module_info.name).load_module(full_package_name)
    else:
        module = sys.modules[full_package_name]

    return module


def start_rack_with_config(start_immediately=True):
    logger = get_logger()
    parser = argparse.ArgumentParser(
        description="Rack starter of the DeviceRepo.")

    parser.add_argument("-c", "--config", dest="config", type=str,
                        help="path to the config file")
    args = parser.parse_args()

    racks_dict = list_all_racks()

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

    rack = DeviceRack("RackStater", host_addr, host_port, logger)

    for dev_init_inst in dev_init_list:
        argv = list(filter(lambda x: x, dev_init_inst.split(" ")))
        dev = argv[0].lower()
        logger.info(f"=> Initializing device {argv[0]}")
        if dev in racks_dict:
            module = get_module(racks_dict[dev][0], racks_dict[dev][1])
            parser = module.get_parser()
            try:
                argv.pop(0)
                args = parser.parse_args(argv)
            except (SystemExit, InvalidParameterException):
                print(f"Error: Invalid initialization instruction for {argv[0]}.")
                parser.print_help()
                exit(1)

            module.load_dev(rack, args, logger)
        else:
            print(f"Error: Device {argv[0]} not found.")
            exit(1)

    logger.info("Initialization finished.")

    if start_immediately:
        rack.start()
    return rack
