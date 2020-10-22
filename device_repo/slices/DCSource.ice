#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    interface DCSource extends Device {
        void set_voltage(double voltage_in_volts);
        double get_voltage();
        void output_on();
        void output_off();
    }
}
