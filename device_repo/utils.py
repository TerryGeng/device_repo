import logging
from functools import wraps

import IcePy
import numpy as np

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


def to_ice_data_type(np_type):
    from device_repo import DataType
    if np_type == np.dtype(np.bool):
        return DataType.Bool
    elif np_type == np.dtype(np.byte):
        return DataType.Byte
    elif np_type == np.dtype(np.short):
        return DataType.Short
    elif np_type == np.dtype(np.int16):
        return DataType.Int
    elif np_type == np.dtype(np.float):
        return DataType.Float
    elif np_type == np.dtype(np.double):
        return DataType.Double
    else:
        raise TypeError("Unknown data type!")


def to_numpy_data_type(ice_type):
    from device_repo import DataType
    if ice_type == DataType.Bool:
        return np.dtype(np.bool)
    elif ice_type == DataType.Byte:
        return np.dtype(np.byte)
    elif ice_type == DataType.Short:
        return np.dtype(np.short)
    elif ice_type == DataType.Int:
        return np.dtype(np.int16)
    elif ice_type == DataType.Float:
        return np.dtype(np.float)
    elif ice_type == DataType.Double:
        return np.dtype(np.double)
    else:
        raise TypeError("Unknown data type!")


def pack_data_set(array):
    from device_repo import DataSet

    if not isinstance(array, np.ndarray):
        array = np.asarray(array)
        data_type = to_ice_data_type(array.dtype)
        packed = array.tobytes()

        return DataSet(array.shape, data_type, packed)


def unpack_data_set(packed):
    from device_repo import DataSet

    if isinstance(packed, DataSet):
        return np.frombuffer(
            packed.packed_data,
            dtype=to_numpy_data_type(packed.type)
        ).reshape(packed.shape)
    elif isinstance(packed, list):
        l = []
        for packed_item in packed:
            if isinstance(packed_item, DataSet):
                l.append(
                    np.frombuffer(
                        packed_item.packed_data,
                        dtype=to_numpy_data_type(packed_item.type)
                    ).reshape(packed_item.shape)
                )
            else:
                raise TypeError("Invalid input! Not a dataset.")
        return l
    else:
        raise TypeError("Invalid input! Not a dataset.")





