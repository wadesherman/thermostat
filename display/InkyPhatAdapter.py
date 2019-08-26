from inky import InkyPHAT


class InkyPhatAdapter(object):
    refresh_interval = 60
    inkyphat = InkyPHAT('red')

    def update(self):
        print("foo")
        self.inkyphat.show()
