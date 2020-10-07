#include<host.ice>

[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    sequence<double> RawWaveform;

    interface AWG extends Device {
        void write_raw_waveform(int channel, double amplitude, RawWaveform waveform);
        void set_channel_offset(int channel, double amplitude, double offset_voltage);
        void set_channel_amplitude(int channel, double amp_in_volts);
        void stop_all();
        void run_all();
        void stop_channel(int channel);
        void run_channel(int channel);
    }
}
