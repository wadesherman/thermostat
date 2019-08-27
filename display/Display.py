from time import sleep
from queue import Queue


class Display(object):
    queue = Queue()

    def __init__(self, display):
        self.display = display

    def notify(self, m):
        self.queue.put(m)

    def loop(self):
        while True:
            item = self.queue.get()
            print(f'display: {item}')
            # item = self.queue.get()
            # print(item)
            # self.display.update()
