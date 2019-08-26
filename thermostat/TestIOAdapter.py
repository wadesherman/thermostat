class TestIOAdapter:

    def __init__(self):
        self.heatRelay = TestDevice("heat")
        self.coolRelay = TestDevice("cool")
        self.fanRelay = TestDevice("fan")


class TestDevice(object):
    def __init__(self, t):
        self.t = t

    def on(self):
        print(self.t + ": on")

    def off(self):
        print(self.t + ": off")
