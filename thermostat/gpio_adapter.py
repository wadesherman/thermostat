from gpiozero import OutputDevice

class GpioAdapter:

  def __init__(self):
    self.heatRelay = OutputDevice(1, initial_value=False)
    self.coolRelay = OutputDevice(2, initial_value=False)
    self.fanRelay = OutputDevice(3, initial_value=False)
