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

    enum DataType {
        Bool,  // 1 bit
        Byte,  // 1 byte = 4 bits
        Short,  // 2 bytes
        Int,  // 4 bytes
        Float,   // 4 bytes
        Double  // 8 bytes
    }

    sequence<byte> bytes;
    sequence<int> ints;
    sequence<double> doubles;
    sequence<string> strings;

    struct DataSet {
        ints shape;
        DataType type;
        bytes packed_data;  // numpy.array([...]).tobytes()
    };
    struct DoubleDataSet {
        ints shape;
        doubles array;
    };
    struct IntDataSet {
        ints shape;
        ints array;
    };
    struct ByteDataSet {
        ints shape;
        bytes array;
    };

    sequence<DataSet> DataSets;
    sequence<DoubleDataSet> DoubleDataSets;
    sequence<IntDataSet> IntDataSets;
    sequence<ByteDataSet> ByteDataSets;
}
