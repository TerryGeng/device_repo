#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    interface DG extends Device {
        // Delay Generator
        void set_cycle_frequency(double freq_in_hz);
        double get_cycle_frequency();
        void set_channel_delay(int channel_index, double rising_at, double fall_after);
        doubles get_channel_delay(int channel_index);  // return [rising_at, fall_after]
    }
}
