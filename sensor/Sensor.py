class Temperature(object):

  def __init__(self, sensor):
    self.sensor = sensor

  def getTemperature(self):
    self.sensor.getTemperature

  def getHumidity(self):
     self.sensor.getHumidity
