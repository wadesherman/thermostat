from abc import ABC, abstractmethod


class ThermostatAdapterInterface(ABC):
    @property
    @abstractmethod
    def heat_relay(self):
        pass

    @property
    @abstractmethod
    def cool_relay(self):
        pass

    @property
    @abstractmethod
    def fan_relay(self):
        pass
