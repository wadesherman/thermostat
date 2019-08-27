from ..SensorAdapterInterface import SensorAdapterInterface

from si7021 import Si7021
from smbus2 import SMBus
from time import time


class Si7021Adapter(SensorAdapterInterface):
    humidity: float
    temperature: float
    last_read: float = 0

    def __init__(self):
        self.sensor = Si7021(SMBus(1))

    def read(self):
        if time() - self.last_read > 30:
            self.humidity, self.temperature = self.sensor.read()
            self.last_read = time()

    def get_temperature(self):
        self.read()
        return self.temperature

    def get_humidity(self):
        self.read()
        return self.humidity
