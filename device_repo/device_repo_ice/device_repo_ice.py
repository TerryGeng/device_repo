# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.4
#
# <auto-generated>
#
# Generated from file `device_repo.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
from . import device_type_ice

# Included module device_repo_ice
_M_device_repo_ice = Ice.openModule('device_repo.device_repo_ice')

# Start of module device_repo_ice
__name__ = 'device_repo.device_repo_ice'

if 'DeviceStatus' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceStatus = Ice.createTempClass()
    class DeviceStatus(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    DeviceStatus.Idle = DeviceStatus("Idle", 0)
    DeviceStatus.Occupied = DeviceStatus("Occupied", 1)
    DeviceStatus.Malfunction = DeviceStatus("Malfunction", 2)
    DeviceStatus._enumerators = { 0:DeviceStatus.Idle, 1:DeviceStatus.Occupied, 2:DeviceStatus.Malfunction }

    _M_device_repo_ice._t_DeviceStatus = IcePy.defineEnum('::device_repo_ice::DeviceStatus', DeviceStatus, (), DeviceStatus._enumerators)

    _M_device_repo_ice.DeviceStatus = DeviceStatus
    del DeviceStatus

if 'DeviceEntry' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceEntry = Ice.createTempClass()
    class DeviceEntry(object):
        def __init__(self, id='', type=_M_device_repo_ice.DeviceType.Dummy):
            self.id = id
            self.type = type

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.id)
            _h = 5 * _h + Ice.getHash(self.type)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_device_repo_ice.DeviceEntry):
                return NotImplemented
            else:
                if self.id is None or other.id is None:
                    if self.id != other.id:
                        return (-1 if self.id is None else 1)
                else:
                    if self.id < other.id:
                        return -1
                    elif self.id > other.id:
                        return 1
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
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
            return IcePy.stringify(self, _M_device_repo_ice._t_DeviceEntry)

        __repr__ = __str__

    _M_device_repo_ice._t_DeviceEntry = IcePy.defineStruct('::device_repo_ice::DeviceEntry', DeviceEntry, (), (
        ('id', (), IcePy._t_string),
        ('type', (), _M_device_repo_ice._t_DeviceType)
    ))

    _M_device_repo_ice.DeviceEntry = DeviceEntry
    del DeviceEntry

_M_device_repo_ice._t_Device = IcePy.defineValue('::device_repo_ice::Device', Ice.Value, -1, (), False, True, None, ())

if 'DevicePrx' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DevicePrx = Ice.createTempClass()
    class DevicePrx(Ice.ObjectPrx):

        def get_type(self, context=None):
            return _M_device_repo_ice.Device._op_get_type.invoke(self, ((), context))

        def get_typeAsync(self, context=None):
            return _M_device_repo_ice.Device._op_get_type.invokeAsync(self, ((), context))

        def begin_get_type(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.Device._op_get_type.begin(self, ((), _response, _ex, _sent, context))

        def end_get_type(self, _r):
            return _M_device_repo_ice.Device._op_get_type.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_device_repo_ice.DevicePrx.ice_checkedCast(proxy, '::device_repo_ice::Device', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_device_repo_ice.DevicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::Device'
    _M_device_repo_ice._t_DevicePrx = IcePy.defineProxy('::device_repo_ice::Device', DevicePrx)

    _M_device_repo_ice.DevicePrx = DevicePrx
    del DevicePrx

    _M_device_repo_ice.Device = Ice.createTempClass()
    class Device(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::device_repo_ice::Device')

        def ice_id(self, current=None):
            return '::device_repo_ice::Device'

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::Device'

        def get_type(self, current=None):
            raise NotImplementedError("servant method 'get_type' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DeviceDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_DeviceDisp = IcePy.defineClass('::device_repo_ice::Device', Device, (), None, ())
    Device._ice_type = _M_device_repo_ice._t_DeviceDisp

    Device._op_get_type = IcePy.Operation('get_type', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_device_repo_ice._t_DeviceType, False, 0), ())

    _M_device_repo_ice.Device = Device
    del Device

if '_t_DeviceEntries' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice._t_DeviceEntries = IcePy.defineSequence('::device_repo_ice::DeviceEntries', (), _M_device_repo_ice._t_DeviceEntry)

if 'InvalidTokenException' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.InvalidTokenException = Ice.createTempClass()
    class InvalidTokenException(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::device_repo_ice::InvalidTokenException'

    _M_device_repo_ice._t_InvalidTokenException = IcePy.defineException('::device_repo_ice::InvalidTokenException', InvalidTokenException, (), False, None, ())
    InvalidTokenException._ice_type = _M_device_repo_ice._t_InvalidTokenException

    _M_device_repo_ice.InvalidTokenException = InvalidTokenException
    del InvalidTokenException

if 'DeviceOccupiedException' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceOccupiedException = Ice.createTempClass()
    class DeviceOccupiedException(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::device_repo_ice::DeviceOccupiedException'

    _M_device_repo_ice._t_DeviceOccupiedException = IcePy.defineException('::device_repo_ice::DeviceOccupiedException', DeviceOccupiedException, (), False, None, ())
    DeviceOccupiedException._ice_type = _M_device_repo_ice._t_DeviceOccupiedException

    _M_device_repo_ice.DeviceOccupiedException = DeviceOccupiedException
    del DeviceOccupiedException

if 'DeviceReacquiredException' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceReacquiredException = Ice.createTempClass()
    class DeviceReacquiredException(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::device_repo_ice::DeviceReacquiredException'

    _M_device_repo_ice._t_DeviceReacquiredException = IcePy.defineException('::device_repo_ice::DeviceReacquiredException', DeviceReacquiredException, (), False, None, ())
    DeviceReacquiredException._ice_type = _M_device_repo_ice._t_DeviceReacquiredException

    _M_device_repo_ice.DeviceReacquiredException = DeviceReacquiredException
    del DeviceReacquiredException

if 'UnknownDeviceException' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.UnknownDeviceException = Ice.createTempClass()
    class UnknownDeviceException(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::device_repo_ice::UnknownDeviceException'

    _M_device_repo_ice._t_UnknownDeviceException = IcePy.defineException('::device_repo_ice::UnknownDeviceException', UnknownDeviceException, (), False, None, ())
    UnknownDeviceException._ice_type = _M_device_repo_ice._t_UnknownDeviceException

    _M_device_repo_ice.UnknownDeviceException = UnknownDeviceException
    del UnknownDeviceException

if 'DeviceException' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceException = Ice.createTempClass()
    class DeviceException(Ice.UserException):
        def __init__(self, msg=''):
            self.msg = msg

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::device_repo_ice::DeviceException'

    _M_device_repo_ice._t_DeviceException = IcePy.defineException('::device_repo_ice::DeviceException', DeviceException, (), False, None, (('msg', (), IcePy._t_string, False, 0),))
    DeviceException._ice_type = _M_device_repo_ice._t_DeviceException

    _M_device_repo_ice.DeviceException = DeviceException
    del DeviceException

if 'WrongParameterException' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.WrongParameterException = Ice.createTempClass()
    class WrongParameterException(Ice.UserException):
        def __init__(self, msg=''):
            self.msg = msg

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::device_repo_ice::WrongParameterException'

    _M_device_repo_ice._t_WrongParameterException = IcePy.defineException('::device_repo_ice::WrongParameterException', WrongParameterException, (), False, None, (('msg', (), IcePy._t_string, False, 0),))
    WrongParameterException._ice_type = _M_device_repo_ice._t_WrongParameterException

    _M_device_repo_ice.WrongParameterException = WrongParameterException
    del WrongParameterException

_M_device_repo_ice._t_DeviceRack = IcePy.defineValue('::device_repo_ice::DeviceRack', Ice.Value, -1, (), False, True, None, ())

if 'DeviceRackPrx' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceRackPrx = Ice.createTempClass()
    class DeviceRackPrx(Ice.ObjectPrx):

        def get_device_prx(self, id, context=None):
            return _M_device_repo_ice.DeviceRack._op_get_device_prx.invoke(self, ((id, ), context))

        def get_device_prxAsync(self, id, context=None):
            return _M_device_repo_ice.DeviceRack._op_get_device_prx.invokeAsync(self, ((id, ), context))

        def begin_get_device_prx(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRack._op_get_device_prx.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_get_device_prx(self, _r):
            return _M_device_repo_ice.DeviceRack._op_get_device_prx.end(self, _r)

        def release_device_prx(self, id, context=None):
            return _M_device_repo_ice.DeviceRack._op_release_device_prx.invoke(self, ((id, ), context))

        def release_device_prxAsync(self, id, context=None):
            return _M_device_repo_ice.DeviceRack._op_release_device_prx.invokeAsync(self, ((id, ), context))

        def begin_release_device_prx(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRack._op_release_device_prx.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_release_device_prx(self, _r):
            return _M_device_repo_ice.DeviceRack._op_release_device_prx.end(self, _r)

        def check_status(self, id, context=None):
            return _M_device_repo_ice.DeviceRack._op_check_status.invoke(self, ((id, ), context))

        def check_statusAsync(self, id, context=None):
            return _M_device_repo_ice.DeviceRack._op_check_status.invokeAsync(self, ((id, ), context))

        def begin_check_status(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRack._op_check_status.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_check_status(self, _r):
            return _M_device_repo_ice.DeviceRack._op_check_status.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_device_repo_ice.DeviceRackPrx.ice_checkedCast(proxy, '::device_repo_ice::DeviceRack', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_device_repo_ice.DeviceRackPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DeviceRack'
    _M_device_repo_ice._t_DeviceRackPrx = IcePy.defineProxy('::device_repo_ice::DeviceRack', DeviceRackPrx)

    _M_device_repo_ice.DeviceRackPrx = DeviceRackPrx
    del DeviceRackPrx

    _M_device_repo_ice.DeviceRack = Ice.createTempClass()
    class DeviceRack(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::device_repo_ice::DeviceRack')

        def ice_id(self, current=None):
            return '::device_repo_ice::DeviceRack'

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DeviceRack'

        def get_device_prx(self, id, current=None):
            raise NotImplementedError("servant method 'get_device_prx' not implemented")

        def release_device_prx(self, id, current=None):
            raise NotImplementedError("servant method 'release_device_prx' not implemented")

        def check_status(self, id, current=None):
            raise NotImplementedError("servant method 'check_status' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DeviceRackDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_DeviceRackDisp = IcePy.defineClass('::device_repo_ice::DeviceRack', DeviceRack, (), None, ())
    DeviceRack._ice_type = _M_device_repo_ice._t_DeviceRackDisp

    DeviceRack._op_get_device_prx = IcePy.Operation('get_device_prx', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_device_repo_ice._t_DevicePrx, False, 0), (_M_device_repo_ice._t_InvalidTokenException, _M_device_repo_ice._t_DeviceOccupiedException))
    DeviceRack._op_release_device_prx = IcePy.Operation('release_device_prx', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, (_M_device_repo_ice._t_InvalidTokenException,))
    DeviceRack._op_check_status = IcePy.Operation('check_status', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_device_repo_ice._t_DeviceStatus, False, 0), (_M_device_repo_ice._t_InvalidTokenException,))

    _M_device_repo_ice.DeviceRack = DeviceRack
    del DeviceRack

_M_device_repo_ice._t_DeviceRepo = IcePy.defineValue('::device_repo_ice::DeviceRepo', Ice.Value, -1, (), False, True, None, ())

if 'DeviceRepoPrx' not in _M_device_repo_ice.__dict__:
    _M_device_repo_ice.DeviceRepoPrx = Ice.createTempClass()
    class DeviceRepoPrx(Ice.ObjectPrx):

        def list_devices(self, context=None):
            return _M_device_repo_ice.DeviceRepo._op_list_devices.invoke(self, ((), context))

        def list_devicesAsync(self, context=None):
            return _M_device_repo_ice.DeviceRepo._op_list_devices.invokeAsync(self, ((), context))

        def begin_list_devices(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRepo._op_list_devices.begin(self, ((), _response, _ex, _sent, context))

        def end_list_devices(self, _r):
            return _M_device_repo_ice.DeviceRepo._op_list_devices.end(self, _r)

        def check_device_status(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_check_device_status.invoke(self, ((id, ), context))

        def check_device_statusAsync(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_check_device_status.invokeAsync(self, ((id, ), context))

        def begin_check_device_status(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRepo._op_check_device_status.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_check_device_status(self, _r):
            return _M_device_repo_ice.DeviceRepo._op_check_device_status.end(self, _r)

        def get_device_type(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_get_device_type.invoke(self, ((id, ), context))

        def get_device_typeAsync(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_get_device_type.invokeAsync(self, ((id, ), context))

        def begin_get_device_type(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRepo._op_get_device_type.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_get_device_type(self, _r):
            return _M_device_repo_ice.DeviceRepo._op_get_device_type.end(self, _r)

        def acquire_device(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_acquire_device.invoke(self, ((id, ), context))

        def acquire_deviceAsync(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_acquire_device.invokeAsync(self, ((id, ), context))

        def begin_acquire_device(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRepo._op_acquire_device.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_acquire_device(self, _r):
            return _M_device_repo_ice.DeviceRepo._op_acquire_device.end(self, _r)

        def release_device(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_release_device.invoke(self, ((id, ), context))

        def release_deviceAsync(self, id, context=None):
            return _M_device_repo_ice.DeviceRepo._op_release_device.invokeAsync(self, ((id, ), context))

        def begin_release_device(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRepo._op_release_device.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_release_device(self, _r):
            return _M_device_repo_ice.DeviceRepo._op_release_device.end(self, _r)

        def list_acquired_devices(self, context=None):
            return _M_device_repo_ice.DeviceRepo._op_list_acquired_devices.invoke(self, ((), context))

        def list_acquired_devicesAsync(self, context=None):
            return _M_device_repo_ice.DeviceRepo._op_list_acquired_devices.invokeAsync(self, ((), context))

        def begin_list_acquired_devices(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRepo._op_list_acquired_devices.begin(self, ((), _response, _ex, _sent, context))

        def end_list_acquired_devices(self, _r):
            return _M_device_repo_ice.DeviceRepo._op_list_acquired_devices.end(self, _r)

        def add_device(self, id, type, rack, access_token, context=None):
            return _M_device_repo_ice.DeviceRepo._op_add_device.invoke(self, ((id, type, rack, access_token), context))

        def add_deviceAsync(self, id, type, rack, access_token, context=None):
            return _M_device_repo_ice.DeviceRepo._op_add_device.invokeAsync(self, ((id, type, rack, access_token), context))

        def begin_add_device(self, id, type, rack, access_token, _response=None, _ex=None, _sent=None, context=None):
            return _M_device_repo_ice.DeviceRepo._op_add_device.begin(self, ((id, type, rack, access_token), _response, _ex, _sent, context))

        def end_add_device(self, _r):
            return _M_device_repo_ice.DeviceRepo._op_add_device.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_device_repo_ice.DeviceRepoPrx.ice_checkedCast(proxy, '::device_repo_ice::DeviceRepo', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_device_repo_ice.DeviceRepoPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DeviceRepo'
    _M_device_repo_ice._t_DeviceRepoPrx = IcePy.defineProxy('::device_repo_ice::DeviceRepo', DeviceRepoPrx)

    _M_device_repo_ice.DeviceRepoPrx = DeviceRepoPrx
    del DeviceRepoPrx

    _M_device_repo_ice.DeviceRepo = Ice.createTempClass()
    class DeviceRepo(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::device_repo_ice::DeviceRepo')

        def ice_id(self, current=None):
            return '::device_repo_ice::DeviceRepo'

        @staticmethod
        def ice_staticId():
            return '::device_repo_ice::DeviceRepo'

        def list_devices(self, current=None):
            raise NotImplementedError("servant method 'list_devices' not implemented")

        def check_device_status(self, id, current=None):
            raise NotImplementedError("servant method 'check_device_status' not implemented")

        def get_device_type(self, id, current=None):
            raise NotImplementedError("servant method 'get_device_type' not implemented")

        def acquire_device(self, id, current=None):
            raise NotImplementedError("servant method 'acquire_device' not implemented")

        def release_device(self, id, current=None):
            raise NotImplementedError("servant method 'release_device' not implemented")

        def list_acquired_devices(self, current=None):
            raise NotImplementedError("servant method 'list_acquired_devices' not implemented")

        def add_device(self, id, type, rack, access_token, current=None):
            raise NotImplementedError("servant method 'add_device' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_device_repo_ice._t_DeviceRepoDisp)

        __repr__ = __str__

    _M_device_repo_ice._t_DeviceRepoDisp = IcePy.defineClass('::device_repo_ice::DeviceRepo', DeviceRepo, (), None, ())
    DeviceRepo._ice_type = _M_device_repo_ice._t_DeviceRepoDisp

    DeviceRepo._op_list_devices = IcePy.Operation('list_devices', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_device_repo_ice._t_DeviceEntries, False, 0), ())
    DeviceRepo._op_check_device_status = IcePy.Operation('check_device_status', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_device_repo_ice._t_DeviceStatus, False, 0), (_M_device_repo_ice._t_UnknownDeviceException,))
    DeviceRepo._op_get_device_type = IcePy.Operation('get_device_type', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_device_repo_ice._t_DeviceType, False, 0), (_M_device_repo_ice._t_UnknownDeviceException,))
    DeviceRepo._op_acquire_device = IcePy.Operation('acquire_device', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_ObjectPrx, False, 0), (_M_device_repo_ice._t_DeviceOccupiedException, _M_device_repo_ice._t_UnknownDeviceException, _M_device_repo_ice._t_DeviceReacquiredException))
    DeviceRepo._op_release_device = IcePy.Operation('release_device', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, (_M_device_repo_ice._t_DeviceOccupiedException, _M_device_repo_ice._t_UnknownDeviceException))
    DeviceRepo._op_list_acquired_devices = IcePy.Operation('list_acquired_devices', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_device_repo_ice._t_DeviceEntries, False, 0), ())
    DeviceRepo._op_add_device = IcePy.Operation('add_device', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), _M_device_repo_ice._t_DeviceType, False, 0), ((), _M_device_repo_ice._t_DeviceRackPrx, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_bool, False, 0), ())

    _M_device_repo_ice.DeviceRepo = DeviceRepo
    del DeviceRepo

# End of module device_repo_ice
