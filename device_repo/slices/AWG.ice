#include<device_repo.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    sequence<double> RawWaveform;

    interface AWG extends Device {
        // Arbitrary Waveform Generator
        void write_raw_waveform(RawWaveform waveform, double amplitude);
        void set_offset(double amplitude, double offset_voltage);
        void set_amplitude(double amp_in_volts);
        void stop();
        void run();
    }
}
