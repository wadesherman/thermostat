from abc import ABC, abstractmethod


class ProtocolInterface(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def loop(self):
        pass