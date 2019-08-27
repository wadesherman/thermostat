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
            item = self.queue.get()
            print(f'thermostat: {item}')
            self.queue.task_done()

    def heat(self):
        while self.values.read("hvac_state") == "heat":
            if self.values.read("current_temperature") < self.values.read("set_temperature"):
                self.io.heat_relay.on()
            else:
                self.io.heat_relay.off()
            sleep(1)

    def cool(self):
        while self.values.read("hvac_state") == "cool":
            if self.values.read("current_temperature") > self.values.read("set_temperature"):
                self.io.cool_relay.on()
            else:
                self.io.cool_relay.off()
            sleep(1)

    def fan(self):
        self.io.fan_relay.on()
        while self.values.read("hvac_state") == "fan":
            sleep(1)
