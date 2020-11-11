import logging
from functools import wraps

import IcePy

logger = None


def get_logger(level=None):
    global logger

    if logger:
        return logger

    logger = logging.getLogger("device_repo")
    map(logger.removeHandler, logger.handlers[:])
    logger.setLevel(level if level else logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s %(levelname)s] "
        "%(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def get_rack_argv_parser(description):
    import argparse
    parser = argparse.ArgumentParser(
        description=description)

    parser.add_argument("--host", dest="host", type=str, default="127.0.0.1",
                        help="address of the device repo host")
    parser.add_argument("--port", dest="port", type=int, default=20201,
                        help="port of the device repo host")

    return parser


def log_invoke_evt(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if isinstance(args[-1], IcePy.Current):
            current = args[-1]
            args_str = str(args[1:-1])
            get_logger().info(f"{f.__name__} invoked by {current.con.toString()}, with "
                              f"parameters {args_str}")

        return f(*args, **kwargs)
    return wrapper


class InvalidParameterException(Exception):
    pass

