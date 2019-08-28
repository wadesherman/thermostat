from abc import ABC, abstractmethod


class ObserverInterface(ABC):
    @abstractmethod
    def notify(self, m):
        pass