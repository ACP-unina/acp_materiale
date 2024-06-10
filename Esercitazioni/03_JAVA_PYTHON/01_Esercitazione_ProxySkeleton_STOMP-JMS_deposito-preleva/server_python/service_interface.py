from abc import ABC, abstractmethod

class IService(ABC):

    @abstractmethod
    def deposita(self, valore):
        pass

    @abstractmethod
    def preleva(self):
        pass