from abc import ABC, abstractmethod


class DataService(ABC):

    @abstractmethod
    def read():
        pass

    @abstractmethod
    def write():
        pass
