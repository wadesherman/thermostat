import threading

class Thermostat(object):
  lock = None
  thread = None
  observers = []
  programs = {
    'heat': self.heat,
    'cool': self.cool,
    'fan': self.fan,
  }
  
  def __init__(self, io, lock):
    self.io = io
    self.lock = lock

  def getSettings(self):
    lock.aquire()
  
  def run(self, program):
    // kill existing thread
    // run new thread

  def kill(self):
    thread.

  def heat(self):
    while True: 
      if(current_temp < set_temp):
        io.heatRelay.on()
      else:
        io.heatRelay.off()
     
  def cool(self):
    while True:
      if(current_temp > set_temp):
        io.coolRelay.on()
      else:
        io.coolRelay.off()

  def fan(self):
    io.fanRelay.on()
    while True:
 
