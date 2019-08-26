from time import sleep


class Display(object):
    def __init__(self, display, lock):
        self.display = display
        self.registerLock = lock

    def loop(self):
        while True:
            self.display.update()
            sleep(self.display.refresh_interval)
