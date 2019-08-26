class Sensor(object):

    def __init__(self, sensor):
        self.sensor = sensor

    def get_temperature(self):
        return self.sensor.get_temperature()

    def get_humidity(self):
        return self.sensor.get_humidity()
