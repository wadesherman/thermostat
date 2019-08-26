import threading
from time import sleep
from queue import Queue


class Thermostat(object):
    values = None
    thread = None
    queue = Queue()

    def __init__(self, io):
        self.io = io
        self.programs = {
            'heat': self.heat,
            'cool': self.cool,
            'fan': self.fan,
        }

    def loop(self):
        while True:
            print(f'thermostat loop')
            # task = self.queue.get()
            # print(task)
            sleep(1)
        # kill existing thread
        # run new thread

    def heat(self):
        while self.values.read("hvac_state") == "heat":
            if self.values.read("current_temperature") < self.values.read("set_temperature"):
                self.io.heatRelay.on()
            else:
                self.io.heatRelay.off()
            sleep(1)

    def cool(self):
        while self.values.read("hvac_state") == "cool":
            if self.values.read("current_temperature") > self.values.read("set_temperature"):
                self.io.coolRelay.on()
            else:
                self.io.coolRelay.off()
            sleep(1)

    def fan(self):
        self.io.fanRelay.on()
        while self.values.read("hvac_state") == "fan":
            sleep(1)
