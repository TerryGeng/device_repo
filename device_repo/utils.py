import logging

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
