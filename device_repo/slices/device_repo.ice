[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    enum DeviceType {
        Dummy,
        ArbitraryWaveformGenerator,
        ParametricSignalGenerator,
        Acquisition,
        VectorNetworkAnalyzer,
        DelayGenerator,
        DCSource
    }

    enum DeviceStatus {
        Idle,
        Occupied,
        Malfunction
    }

    struct DeviceEntry {
        string id;
        DeviceType type;
    }

    interface Device {
        DeviceType get_type();
    }

    sequence<byte> bytes;
    sequence<double> doubles;
    sequence<string> strings;

    sequence<DeviceEntry> DeviceEntries;

    exception InvalidTokenException {};
    exception DeviceOccupiedException {};
    exception UnknownDeviceException {};

    interface DeviceRack {
        // -- for device repo --
        Device* get_device_prx(string id) throws InvalidTokenException, DeviceOccupiedException;
        void release_device_prx(string id) throws InvalidTokenException;
        DeviceStatus check_status(string id) throws InvalidTokenException;
    }

    interface DeviceRepo {
        // --- for device users ---
        DeviceEntries list_devices();
        DeviceStatus check_device_status(string id) throws UnknownDeviceException;
        DeviceType get_device_type(string id) throws UnknownDeviceException;
        Object* acquire_device(string id) throws DeviceOccupiedException, UnknownDeviceException;
        void release_device(string id) throws DeviceOccupiedException, UnknownDeviceException;
        DeviceEntries list_acquired_devices();

        // --- for devices ---
        bool add_device(string id, DeviceType type, DeviceRack* rack, string access_token);
    }
}
