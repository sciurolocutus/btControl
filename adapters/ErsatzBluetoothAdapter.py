import random

from adapters.BluetoothAdapter import BluetoothAdapter
from dto.bt.Device import Device


class ErsatzBluetoothAdapter(BluetoothAdapter):
    names = ['Ghost', 'BTSpkr2020', 'Phat Beets']

    def list_bt_devices(self):
        return [self.rand_device() for i in range(4)]

    @classmethod
    def rand_device(cls):
        m = cls.rand_mac()
        n = cls.rand_name()
        nick = ''
        d = Device(m, n, nick)
        return d

    @classmethod
    def rand_name(cls):
        return cls.names[random.randint(0, len(cls.names)-1)]

    @classmethod
    def rand_mac(cls):
        return '%02x:%02x:%02x:%02x:%02x:%02x' % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

