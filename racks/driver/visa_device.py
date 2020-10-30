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
    def __init__(self, visa_dev: pyvisa.resources.MessageBasedResource, logger=None):
        self.visa_dev = visa_dev
        self.logger = logger

    def visa_query(self, query, current=None):
        return self.visa_dev.query(query)

    def visa_write(self, cmd, current=None):
        return self.visa_dev.write(cmd)

    def visa_error(self, current=None):
        return self.visa_dev.write("SYST:ERR?")

    def visa_query_ascii_array(self, query, converter=u'f', separator=',',
                               container=list, delay=None):
        # https://pyvisa.readthedocs.io/en/1.8/api/resources.html#pyvisa.resources.MessageBasedResource.query_ascii_values
        ret = self.visa_dev.query_ascii_values(query, converter, separator,
                                               container, delay)
        return ret
