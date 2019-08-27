from ..SensorAdapterInterface import SensorAdapterInterface

import Adafruit_DHT
from time import time


class DHTAdapter(SensorAdapterInterface):
    humidity: float
    temperature: float
    last_read: float = 0
    sensors = {
        "DHT22": Adafruit_DHT.DHT22,
        "DHT11": Adafruit_DHT.DHT11,
        "AM2302": Adafruit_DHT.AM2302,
    }

    def __init__(self, sensor, pin):
        self.pin = pin
        self.sensor = self.sensors[sensor]

    def read(self):
        if time() - self.last_read > 30:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            self.last_read = time()

    def get_temperature(self):
        self.read()
        return self.temperature

    def get_humidity(self):
        self.read()
        return self.humidity
