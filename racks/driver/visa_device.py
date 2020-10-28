import pyvisa
from device_repo import VisaDeviceTemplate
from device_repo.utils import log_invoke_evt

resource_mgr = None


def get_device_by_address(address):
    global resource_mgr
    if not resource_mgr:
        resource_mgr = pyvisa.ResourceManager()

    return resource_mgr.open_resource(address)


class VisaDeviceBase(VisaDeviceTemplate):
    def __init__(self, visa_dev: pyvisa.Resource, logger=None):
        self.visa_dev = visa_dev
        self.logger = logger

    @log_invoke_evt
    def visa_query(self, query, current=None):
        return self.visa_dev.query(query)

    @log_invoke_evt
    def visa_write(self, cmd, current=None):
        return self.visa_dev.write(cmd)
