from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def request(self, data):
        pass