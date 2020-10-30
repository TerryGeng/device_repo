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
}
