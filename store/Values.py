import threading


class Values(object):
    lock = threading.Lock()
    dict = {
        "current_temperature": None,
        "current_humidity": None,
        "state": None,
        "hvac_state": None,
        "set_temperature": None,
    }
    observers = []

    def read(self, key):
        self.lock.acquire()
        val = self.dict[key]
        self.lock.release()
        return val

    def write(self, key, value):
        self.lock.acquire()
        if key in self.dict and self.dict[key] != value:
            self.dict[key] = value
            self.notify_observers({key: value})
        self.lock.release()

    def broadcast_values(self):
        self.lock.acquire()
        for key, value in self.dict.items():
            self.notify_observers({key: value})
        self.lock.release()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, i):
        for o in self.observers:
            o.notify(i)
