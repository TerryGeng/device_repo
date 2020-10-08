import time
import unittest.mock
import threading
import pytest
import Ice

from device_repo.utils import get_logger

logger = get_logger()


class TestDummy:
    @unittest.mock.patch('sys.argv', ['./devicerepo', '-b', '127.0.0.1', '-p', '20201'])
    def start_host(self):
        import device_repo.host
        logger.info("Starting device repo host...")
        host = device_repo.host.main(False)
        threading.Thread(name="Host", target=host.start, daemon=True).start()
        return host

    def get_access(self):
        from device_repo.access import DeviceRepoAccess
        logger.info("Creating device access...")
        access = DeviceRepoAccess("127.0.0.1", "20201")
        return access

    def start_dummy_rack(self):
        from racks.dummy_rack import start_dummy_rack
        rack = start_dummy_rack("127.0.0.1", 20201, False)
        threading.Thread(name="DummyRack", target=rack.start).start()
        time.sleep(0.5)
        return rack

    def test_host_access(self):
        host = self.start_host()
        access = self.get_access()
        assert len(access.list_device()) == 0
        host.ic.shutdown()

    def test_rack_create(self):
        from device_repo import DeviceStatus
        host = self.start_host()
        access = self.get_access()
        assert len(access.list_device()) == 0
        rack = self.start_dummy_rack()

        dev_list = access.list_device()
        assert len(dev_list) == 1
        assert dev_list[0].id == 'Dummy01'
        assert access.get_device_status('Dummy01') == DeviceStatus.Idle

        rack.ic.shutdown()
        host.ic.shutdown()

    def test_device_auto_remove(self):
        host = self.start_host()
        access = self.get_access()
        assert len(access.list_device()) == 0
        rack = self.start_dummy_rack()

        dev_list = access.list_device()
        assert len(dev_list) == 1

        rack.ic.shutdown()
        time.sleep(0.2)
        assert len(access.list_device()) == 0
        host.ic.shutdown()

    def test_get_device(self):
        host = self.start_host()
        rack = self.start_dummy_rack()
        access = self.get_access()
        dev = access.get_device('Dummy01')

        from device_repo import DummyDevice
        assert isinstance(dev, DummyDevice)
        assert dev.get_data() == b'Hello world!'

        access.release_device('Dummy01')

        with pytest.raises(Ice.ObjectNotExistException):
            dev.get_data()

        rack.ic.shutdown()
        host.ic.shutdown()

    def test_device_conflict(self):
        import device_repo
        from device_repo import DeviceStatus
        from device_repo.access import DeviceRepoAccess

        host = self.start_host()
        rack = self.start_dummy_rack()

        access1 = DeviceRepoAccess("127.0.0.1", "20201")
        access2 = DeviceRepoAccess("127.0.0.1", "20201")

        access1.get_device('Dummy01')
        assert 'Dummy01' in host.device_user_map
        assert access1.get_device_status('Dummy01') == DeviceStatus.Occupied
        assert access2.get_device_status('Dummy01') == DeviceStatus.Occupied

        with pytest.raises(device_repo.DeviceOccupiedException):
            access2.get_device('Dummy01')

        access1.release_device('Dummy01')
        assert 'Dummy01' not in host.device_user_map

        dev = access2.get_device('Dummy01')
        assert dev.get_data() == b'Hello world!'

        rack.ic.shutdown()
        host.ic.shutdown()

    def test_client_disconnect(self):
        from device_repo import DeviceStatus
        from device_repo.access import DeviceRepoAccess

        host = self.start_host()
        rack = self.start_dummy_rack()

        access1 = DeviceRepoAccess("127.0.0.1", "20201")
        access2 = DeviceRepoAccess("127.0.0.1", "20201")

        access1.get_device('Dummy01')
        del access1
        time.sleep(0.2)

        assert 'Dummy01' not in host.device_user_map
        assert access2.get_device_status('Dummy01') == DeviceStatus.Idle

        access2.get_device('Dummy01')

        rack.ic.shutdown()
        host.ic.shutdown()

    def test_rack_reconnect(self):
        host = self.start_host()
        rack = self.start_dummy_rack()
        host.ic.shutdown()

        time.sleep(2)
        host = self.start_host()
        time.sleep(2)

        access = self.get_access()
        assert len(access.list_device()) == 1

        rack.ic.shutdown()
        host.ic.shutdown()

