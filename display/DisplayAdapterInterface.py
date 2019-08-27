from abc import ABC, abstractmethod


class DisplayAdapterInterface(ABC):
    @abstractmethod
    def refresh_interval(self):
        pass

    @abstractmethod
    def update(self):
        pass
