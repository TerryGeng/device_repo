[["python:pkgdir:device_repo_ice"]]

module device_repo_ice {
    enum DeviceType {
        Dummy,
        ArbitraryWaveformGenerator,
        ParametricSignalGenerator,
        Digitizer,
        VectorNetworkAnalyzer,
        DelayGenerator,
        DCSource
    }

    sequence<byte> bytes;
    sequence<int> ints;
    sequence<double> doubles;
    sequence<string> strings;

    struct DoubleDataSet {
        ints shape;
        doubles array;
    };

    sequence<DoubleDataSet> DoubleDataSets;
}
