#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    interface VNA extends Device {
        // Vector Network Analyzer

        void set_power(double power_in_db);
        double get_power();

        void set_frequency_center(double freq_in_hz);
        double get_frequency_center();

        void set_frequency_start(double freq_in_hz);
        double get_frequency_start();

        void set_frequency_stop(double freq_in_hz);
        double get_frequency_stop();

        doubles get_s(int channel);

        void set_num_of_points(int num_of_points);
        double get_num_of_points();

        void sweep_on();
        void sweep_off();
    }
}
