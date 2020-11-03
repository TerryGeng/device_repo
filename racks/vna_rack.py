from device_repo import VNA, VNATemplate, DeviceRack, DeviceType
from device_repo.utils import get_logger, get_rack_argv_parser, log_invoke_evt

if __name__ == "__main__":
    from driver.visa_device import VisaDeviceBase, get_device_by_address
else:
    from .driver.visa_device import VisaDeviceBase, get_device_by_address


class VNA_Keysight(VNATemplate, VisaDeviceBase):
    def __init__(self, name, dev):
        super().__init__(dev)
        self.name = name

    def get_type(self, current=None):
        return DeviceType.VectorNetworkAnalyzer

    @log_invoke_evt
    def set_power(self, power_in_db, current=None):
        self.visa_write(f":SOUR:POW {power_in_db:.8e}dB")

    @log_invoke_evt
    def get_power(self, current=None):
        return float(self.visa_query(":SOUR:POW?"))

    @log_invoke_evt
    def set_frequency_center(self, freq_in_hz, current=None):
        self.visa_write(f":SOUR:FREQ:CENT {freq_in_hz:.13e}Hz")

    @log_invoke_evt
    def get_frequency_center(self, current=None):
        return float(self.visa_query(":SENS:FREQ:CENT?"))

    @log_invoke_evt
    def set_frequency_start(self, freq_in_hz, current=None):
        self.visa_write(f":SOUR:FREQ:STAR {freq_in_hz:.13e}Hz")

    @log_invoke_evt
    def get_frequency_start(self, current=None):
        return float(self.visa_query(":SENS:FREQ:STAR?"))

    @log_invoke_evt
    def set_frequency_stop(self, freq_in_hz, current=None):
        self.visa_write(f":SOUR:FREQ:STOP {freq_in_hz:.13e}Hz")

    @log_invoke_evt
    def get_frequency_stop(self, current=None):
        return float(self.visa_query(":SENS:FREQ:STOP?"))

    @log_invoke_evt
    def get_s(self, channel, current=None):
        msg = self.visa_query(f':CALC{channel}:PAR:CAT?').strip('"')
        measname = msg.split(',')[0]
        self.visa_write(f':CALC{channel}:PAR:SEL "{measname}"')

        self.sweep_off()
        self.visa_write(":INIT:IMM")
        self.visa_write("*WAI")
        self.visa_write(":FORMAT:BORD NORM")
        self.visa_write(":FORMAT ASCII")

        data = self.visa_query_ascii_array(f":CALC{channel}:DATA? SDATA")

        return data

    @log_invoke_evt
    def set_num_of_points(self, num_of_points, current=None):
        self.visa_write(f"SOUR:SEW:POIN {num_of_points:d}")

    @log_invoke_evt
    def get_num_of_points(self, current=None):
        return int(self.visa_query("SENS:SWE:POIN?"))

    @log_invoke_evt
    def sweep_on(self, current=None):
        self.visa_write("INIT:CONT ON")

    @log_invoke_evt
    def sweep_off(self, current=None):
        self.visa_write("INIT:CONT OFF")


class VNA_E8363B(VNA_Keysight):
    def __init__(self, name, dev):
        super().__init__(name, dev)
        dev.read_termination = '\n'


model_class_map = {
    'E8363B': VNA_E8363B,
    'N5232B': VNA_Keysight
}


def get_parser():
    model_supported = ", ".join(model_class_map.keys())
    parser = get_rack_argv_parser("Start the general VNA rack.")

    parser.add_argument("model_name_address", nargs="+", type=str,
                        help="model, name and VISA address of the VNA, in the format of "
                             "model:{name}@{address} (multiple instances can be loaded). "
                             f"Model supported: {model_supported}."
                        )
    return parser


def load_dev(rack, args=None, logger=None):
    model_name_address_tuples = []

    for name_addr in args.model_name_address:
        try:
            splited = name_addr.split("@")
            model, name = splited[0].split(":")
            address = splited[1]
            model_name_address_tuples.append((model, name, address))
        except (ValueError, IndexError):
            parser.print_help()
            exit(1)

    for model, name, addr in model_name_address_tuples:
        dev = get_device_by_address(addr)
        identifier = f"VNA_{model}_{name}"

        if logger:
            logger.info(f"Initializing {identifier} at {addr}...")

        if model.upper() in model_class_map:
            vna = model_class_map[model.upper()](identifier, dev)
            rack.load_device(identifier, vna)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    logger = get_logger()
    rack = DeviceRack("VNARack", args.host, args.port, logger)

    load_dev(rack, args, logger)

    rack.start()
