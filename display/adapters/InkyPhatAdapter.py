from ..DisplayAdapterInterface import DisplayAdapterInterface

from inky import InkyPHAT


class InkyPhatAdapter(DisplayAdapterInterface):
    refresh_interval = 60
    inkyphat = InkyPHAT('red')

    def update(self):
        print("foo")
        self.inkyphat.show()
