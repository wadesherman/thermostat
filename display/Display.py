class Display(object):
  def __init__(self, display):
    self.display = display

  def loop(self):
    while True:
      self.display.update()
      sleep(self.display.refreshInterval)
  
