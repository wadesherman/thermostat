from abc import ABC, abstractmethod


class SensorAdapterInterface(ABC):
    @abstractmethod
    def get_temperature(self):
        pass

    @abstractmethod
    def get_humidity(self):
        pass
