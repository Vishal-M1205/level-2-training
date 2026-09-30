from abc import ABC, abstractmethod


class DataRepository(ABC):

    @abstractmethod
    def read():
        pass

    @abstractmethod
    def write():
        pass
