from time import sleep
from queue import Queue


class Display(object):
    queue = Queue()

    def __init__(self, display):
        self.display = display

    def loop(self):
        while True:
            print(f'display loop')
            # item = self.queue.get()
            # print(item)
            # self.display.update()
            sleep(self.display.refresh_interval)


from abc import ABC, abstractmethod


class DisplayAdapterInterface(ABC):
    @property
    @abstractmethod
    def refresh_interval(self):
        pass

    @abstractmethod
    def update(self):
        pass
