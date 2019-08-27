from ..SensorAdapterInterface import SensorAdapterInterface

from time import time
from random import randint


class TestSensorAdapter(SensorAdapterInterface):
    humidity: int
    temperature: int
    last_read: float = 0

    def read(self):
        if time() - self.last_read > 30:
            self.humidity, self.temperature = (randint(60, 65), randint(72, 80))
            self.last_read = time()

    def get_temperature(self):
        self.read()
        return self.temperature

    def get_humidity(self):
        self.read()
        return self.humidity
