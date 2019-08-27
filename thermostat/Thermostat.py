import threading
from time import sleep
from queue import Queue


class Thermostat(object):
    values = {}
    hvac_thread = None
    stop_thread = False
    queue = Queue()

    def __init__(self, io):
        self.io = io
        self.programs = {
            "heat": self.heat,
            "cool": self.cool,
            "fan": self.fan,
        }

    def notify(self, m):
        self.queue.put(m)

    def loop(self):
        while True:
            item = self.queue.get()
            self.values.update(item)

            if "hvac_state" in item or "state" in item:
                self.stop_thread = True
                try:
                    self.hvac_thread.join()
                except AttributeError:
                    pass
                self.stop_thread = False
                if self.values["state"] == "on" and all(v in self.values for v in ("set_temperature", "current_temperature", "hvac_state")):
                    func = getattr(self, self.values["hvac_state"], lambda f: print(f))
                    self.hvac_thread = threading.Thread(target=func)
                    self.hvac_thread.start()
            self.queue.task_done()

    def heat(self):
        while not self.stop_thread:
            if self.values["current_temperature"] < self.values["set_temperature"]:
                self.io.heat_relay.on()
            else:
                self.io.heat_relay.off()
            sleep(1)
        self.io.heat_relay.off()

    def cool(self):
        while not self.stop_thread:
            if self.values["current_temperature"] > self.values["set_temperature"]:
                self.io.cool_relay.on()
            else:
                self.io.cool_relay.off()
            sleep(1)
        self.io.cool_relay.off()

    def fan(self):
        self.io.fan_relay.on()
        while not self.stop_thread:
            sleep(1)
        self.io.fan_relay.off()
