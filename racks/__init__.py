def get_device_module():
    from . import dummy_rack
    from . import psg_rack
    from . import keysight_sd1_rack
    from . import dc_srs_rack

    device_module = {
        "dummy": dummy_rack,
        "psg": psg_rack,
        "keysightsd1": keysight_sd1_rack,
        "dc_srs": dc_srs_rack
    }

    return device_module
