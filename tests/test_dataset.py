import numpy as np


class TestDataset:
    def test_pack_unpack_bytes_1d(self):
        from device_repo.utils import pack_data_set, unpack_data_set
        from device_repo import DataSet, DataType

        mock_set = np.array([0, 1, 2, 3, 4], dtype='byte')
        packed = pack_data_set(mock_set)

        assert isinstance(packed, DataSet)
        assert packed.shape == (5,)
        assert packed.type == DataType.Byte

        unpacked = unpack_data_set(packed)
        assert isinstance(unpacked, np.ndarray)
        assert all(mock_set == unpacked)

    def test_pack_unpack_bytes_2d(self):
        from device_repo.utils import pack_data_set, unpack_data_set
        from device_repo import DataSet, DataType

        mock_set = np.array(
            [[0, 1, 2, 3, 4],
             [5, 6, 7, 8, 9]], dtype='byte')

        packed = pack_data_set(mock_set)

        assert isinstance(packed, DataSet)
        assert packed.shape == (2, 5)
        assert packed.type == DataType.Byte

        unpacked = unpack_data_set(packed)
        assert isinstance(unpacked, np.ndarray)
        assert all((mock_set == unpacked).flatten())

    def test_pack_unpack_bytes_list(self):
        from device_repo.utils import pack_data_set, unpack_data_set
        from device_repo import DataSet, DataType

        mock_set = []
        mock_set.append(np.array([0, 1, 2, 3, 4], dtype='byte'))
        mock_set.append(np.array([1, 2, 3, 4, 5], dtype='byte'))
        mock_set.append(np.array([2, 3, 4, 5, 6], dtype='byte'))

        packed = [pack_data_set(mock) for mock in mock_set]

        assert all([isinstance(item, DataSet) for item in packed])
        assert all([item.shape == (5, ) for item in packed])
        assert all([item.type == DataType.Byte for item in packed])

        unpacked = unpack_data_set(packed)
        assert isinstance(unpacked, list)
        for mock, unpacked_item in zip(mock_set, unpacked):
            assert all((mock == unpacked_item).flatten())



