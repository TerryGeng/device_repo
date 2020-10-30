#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    interface VisaDevice extends Device {
        strings visa_query();
        void visa_write();
        string visa_error();
    }
}
