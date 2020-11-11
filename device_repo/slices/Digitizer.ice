#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    interface Digitizer extends Device {
        void set_sample_number(int number_of_samples);
        void set_input_range(int channel, double range);
        void set_repeats(int repeats);
        void set_trigger_level(double trigger_level);
        void set_trigger_delay(double delay);
        void set_trigger_timeout(double timeout);

        double get_sample_rate(); // in Hz
        int get_sample_number();
        int get_input_range(int channel);
        int get_repeats();
        double get_trigger_level();
        double get_trigger_delay();
        double get_trigger_timeout();

        void start_acquire();
        DoubleDataSets acquire_and_fetch_average();
        DoubleDataSets fetch_average();
        DoubleDataSets acquire_and_fetch();
        DoubleDataSets fetch();
    }
}
