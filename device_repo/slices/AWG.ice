#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    sequence<double> RawWaveform;

    interface AWG extends Device {
        // Arbitrary Waveform Generator
        double get_sample_rate();
        void write_raw_waveform(RawWaveform waveform, double amplitude);
        void set_offset(double offset_voltage);
        double get_offset();
        void set_amplitude(double amp_in_volts);
        double get_amplitude();
        void stop();
        void run();
    }
}
