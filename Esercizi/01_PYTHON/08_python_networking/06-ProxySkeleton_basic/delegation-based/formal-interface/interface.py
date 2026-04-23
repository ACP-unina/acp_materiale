from abc import ABC, abstractmethod

class ServiceInterface(ABC):

    @abstractmethod
    def inverti_stringa(self, data):
        pass