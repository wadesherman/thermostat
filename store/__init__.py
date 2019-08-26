import threading

class Values(object):
    lock = threading.Lock()
    dict = {}

    def initialize(self, key, default = None):
        self.lock.acquire()
        self.dict[key] = default
        self.lock.release()

    def read(self, key):
        self.lock.acquire()
        val = self.dict[key]
        self.lock.release()
        return val

    def write(self, key, value):
        self.lock.acquire()
        self.dict[key] = value
        self.lock.release()
