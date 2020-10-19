#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    interface PSG extends Device {
        // Parametric Signal Generator
        void set_frequency(double freq_in_hz);
        double get_frequency();
        void set_power(double power_in_db);
        double get_power();
        void stop();
        void run();
    }
}
