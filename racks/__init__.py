def get_device_module():
    def get_dummy_module():
        from . import dummy_rack
        return dummy_rack

    def get_psg_module():
        from . import psg_rack
        return psg_rack

    def get_keysight_sd1_module():
        from . import keysight_sd1_rack
        return keysight_sd1_rack

    def get_dc_srs_module():
        from . import dc_srs_rack
        return dc_srs_rack

    def get_vna_module():
        from . import vna_rack
        return vna_rack

    def get_alazar_module():
        from . import alazar_rack
        return alazar_rack

    def get_dg645_module():
        from . import dg645_rack

    device_module_getter = {
        "dummy": get_dummy_module,
        "psg": get_psg_module,
        "keysightsd1": get_keysight_sd1_module,
        "dc_srs": get_dc_srs_module,
        "vna": get_vna_module,
        "alazar": get_alazar_module,
        "dg645": get_dg645_module
    }

    return device_module_getter
