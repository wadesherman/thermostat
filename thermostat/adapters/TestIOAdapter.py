from ..ThermostatAdapterInterface import ThermostatAdapterInterface


class TestDevice(object):
    def __init__(self, t):
        self.t = t

    def on(self):
        print(self.t + ": on")

    def off(self):
        print(self.t + ": off")


class TestIOAdapter(ThermostatAdapterInterface):
    heat_relay = TestDevice("heat")
    cool_relay = TestDevice("cool")
    fan_relay = TestDevice("fan")
