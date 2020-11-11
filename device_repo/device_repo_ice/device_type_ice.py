# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `device_type.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module device_repo_ice
_M_device_repo_ice = Ice.openModule('device_repo.device_repo_ice')
__name__ = 'device_repo.device_repo_ice'

if 'DeviceType' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceType = Ice.createTempClass()
    class DeviceType(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    DeviceType.Dummy = DeviceType("Dummy", 0)
    DeviceType.ArbitraryWaveformGenerator = DeviceType("ArbitraryWaveformGenerator", 1)
    DeviceType.ParametricSignalGenerator = DeviceType("ParametricSignalGenerator", 2)
    DeviceType.Digitizer = DeviceType("Digitizer", 3)
    DeviceType.VectorNetworkAnalyzer = DeviceType("VectorNetworkAnalyzer", 4)
    DeviceType.DelayGenerator = DeviceType("DelayGenerator", 5)
    DeviceType.DCSource = DeviceType("DCSource", 6)
    DeviceType._enumerators = { 0:DeviceType.Dummy, 1:DeviceType.ArbitraryWaveformGenerator, 2:DeviceType.ParametricSignalGenerator, 3:DeviceType.Digitizer, 4:DeviceType.VectorNetworkAnalyzer, 5:DeviceType.DelayGenerator, 6:DeviceType.DCSource }

    _M_device_repo_ice._t_DeviceType = IcePy.defineEnum('::device_repo_ice::DeviceType', DeviceType, (), DeviceType._enumerators)

    _M_device_repo_ice.DeviceType = DeviceType
    del DeviceType

if 'DataType' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DataType = Ice.createTempClass()
    class DataType(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    DataType.Bool = DataType("Bool", 0)
    DataType.Byte = DataType("Byte", 1)
    DataType.Short = DataType("Short", 2)
    DataType.Int = DataType("Int", 3)
    DataType.Float = DataType("Float", 4)
    DataType.Double = DataType("Double", 5)
    DataType._enumerators = { 0:DataType.Bool, 1:DataType.Byte, 2:DataType.Short, 3:DataType.Int, 4:DataType.Float, 5:DataType.Double }

    _M_device_repo_ice._t_DataType = IcePy.defineEnum('::device_repo_ice::DataType', DataType, (), DataType._enumerators)

    _M_device_repo_ice.DataType = DataType
    del DataType

if '_t_bytes' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_bytes = IcePy.defineSequence('::device_repo_ice::bytes', (), IcePy._t_byte)

if '_t_ints' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_ints = IcePy.defineSequence('::device_repo_ice::ints', (), IcePy._t_int)

if '_t_doubles' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_doubles = IcePy.defineSequence('::device_repo_ice::doubles', (), IcePy._t_double)

if '_t_strings' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_strings = IcePy.defineSequence('::device_repo_ice::strings', (), IcePy._t_string)

if 'DataSet' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DataSet = Ice.createTempClass()
    class DataSet(object):
        def __init__(self, shape=None, type=_M_device_repo_ice.DataType.Bool, packed_data=None):
            self.shape = shape
            self.type = type
            self.packed_data = packed_data

        def __hash__(self):
            _h = 0
            if self.shape:
                for _i0 in self.shape:
                    _h = 5 * _h + Ice.getHash(_i0)
            _h = 5 * _h + Ice.getHash(self.type)
            if self.packed_data:
                for _i1 in self.packed_data:
                    _h = 5 * _h + Ice.getHash(_i1)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_device_repo_ice.DataSet):
                return NotImplemented
            else:
                if self.shape is None or other.shape is None:
                    if self.shape != other.shape:
                        return (-1 if self.shape is None else 1)
                else:
                    if self.shape < other.shape:
                        return -1
                    elif self.shape > other.shape:
                        return 1
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
                        return 1
                if self.packed_data is None or other.packed_data is None:
                    if self.packed_data != other.packed_data:
                        return (-1 if self.packed_data is None else 1)
                else:
                    if self.packed_data < other.packed_data:
                        return -1
                    elif self.packed_data > other.packed_data:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DataSet)

        __repr__ = __str__

    _M_device_repo_ice._t_DataSet = IcePy.defineStruct('::device_repo_ice::DataSet', DataSet, (), (
        ('shape', (), _M_device_repo_ice._t_ints),
        ('type', (), _M_device_repo_ice._t_DataType),
        ('packed_data', (), _M_device_repo_ice._t_bytes)
    ))

    _M_device_repo_ice.DataSet = DataSet
    del DataSet

if 'DoubleDataSet' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DoubleDataSet = Ice.createTempClass()
    class DoubleDataSet(object):
        def __init__(self, shape=None, array=None):
            self.shape = shape
            self.array = array

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_device_repo_ice.DoubleDataSet):
                return NotImplemented
            else:
                if self.shape != other.shape:
                    return False
                if self.array != other.array:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DoubleDataSet)

        __repr__ = __str__

    _M_device_repo_ice._t_DoubleDataSet = IcePy.defineStruct('::device_repo_ice::DoubleDataSet', DoubleDataSet, (), (
        ('shape', (), _M_device_repo_ice._t_ints),
        ('array', (), _M_device_repo_ice._t_doubles)
    ))

    _M_device_repo_ice.DoubleDataSet = DoubleDataSet
    del DoubleDataSet

if 'IntDataSet' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.IntDataSet = Ice.createTempClass()
    class IntDataSet(object):
        def __init__(self, shape=None, array=None):
            self.shape = shape
            self.array = array

        def __hash__(self):
            _h = 0
            if self.shape:
                for _i0 in self.shape:
                    _h = 5 * _h + Ice.getHash(_i0)
            if self.array:
                for _i1 in self.array:
                    _h = 5 * _h + Ice.getHash(_i1)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_device_repo_ice.IntDataSet):
                return NotImplemented
            else:
                if self.shape is None or other.shape is None:
                    if self.shape != other.shape:
                        return (-1 if self.shape is None else 1)
                else:
                    if self.shape < other.shape:
                        return -1
                    elif self.shape > other.shape:
                        return 1
                if self.array is None or other.array is None:
                    if self.array != other.array:
                        return (-1 if self.array is None else 1)
                else:
                    if self.array < other.array:
                        return -1
                    elif self.array > other.array:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_IntDataSet)

        __repr__ = __str__

    _M_device_repo_ice._t_IntDataSet = IcePy.defineStruct('::device_repo_ice::IntDataSet', IntDataSet, (), (
        ('shape', (), _M_device_repo_ice._t_ints),
        ('array', (), _M_device_repo_ice._t_ints)
    ))

    _M_device_repo_ice.IntDataSet = IntDataSet
    del IntDataSet

if 'ByteDataSet' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.ByteDataSet = Ice.createTempClass()
    class ByteDataSet(object):
        def __init__(self, shape=None, array=None):
            self.shape = shape
            self.array = array

        def __hash__(self):
            _h = 0
            if self.shape:
                for _i0 in self.shape:
                    _h = 5 * _h + Ice.getHash(_i0)
            if self.array:
                for _i1 in self.array:
                    _h = 5 * _h + Ice.getHash(_i1)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_device_repo_ice.ByteDataSet):
                return NotImplemented
            else:
                if self.shape is None or other.shape is None:
                    if self.shape != other.shape:
                        return (-1 if self.shape is None else 1)
                else:
                    if self.shape < other.shape:
                        return -1
                    elif self.shape > other.shape:
                        return 1
                if self.array is None or other.array is None:
                    if self.array != other.array:
                        return (-1 if self.array is None else 1)
                else:
                    if self.array < other.array:
                        return -1
                    elif self.array > other.array:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_ByteDataSet)

        __repr__ = __str__

    _M_device_repo_ice._t_ByteDataSet = IcePy.defineStruct('::device_repo_ice::ByteDataSet', ByteDataSet, (), (
        ('shape', (), _M_device_repo_ice._t_ints),
        ('array', (), _M_device_repo_ice._t_bytes)
    ))

    _M_device_repo_ice.ByteDataSet = ByteDataSet
    del ByteDataSet

if '_t_DataSets' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_DataSets = IcePy.defineSequence('::device_repo_ice::DataSets', (), _M_device_repo_ice._t_DataSet)

if '_t_DoubleDataSets' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_DoubleDataSets = IcePy.defineSequence('::device_repo_ice::DoubleDataSets', (), _M_device_repo_ice._t_DoubleDataSet)

if '_t_IntDataSets' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_IntDataSets = IcePy.defineSequence('::device_repo_ice::IntDataSets', (), _M_device_repo_ice._t_IntDataSet)

if '_t_ByteDataSets' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_ByteDataSets = IcePy.defineSequence('::device_repo_ice::ByteDataSets', (), _M_device_repo_ice._t_ByteDataSet)

# End of module device_repo_ice
