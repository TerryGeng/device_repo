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
        UInt8,  // 1 bytes
        UInt16,  // 2 bytes
        UInt32,  // 4 bytes
        UInt64,  // 8 bytes
        Int8,  // 1 bytes
        Int16,  // 2 bytes
        Int32,  // 4 bytes
        Int64,  // 8 bytes
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
