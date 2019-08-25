import board
import busio
import adafruit_si7021

class Si7021(object):

  def __init__(self):
    self.i2c = busio.I2C(board.SCL, board.SDA)
    self.sensor = adafruit_si7021.SI7021(i2c)
 
  def getTemperature(self):
    self.sensor.temperature

  def getHumidity(self):
    self.sensor.relative_humidity
 
