#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    interface DummyDevice extends Device {
        bytes get_data();
    }
}
