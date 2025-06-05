from abc import ABC, abstractmethod

class Service(ABC):
    
    @abstractmethod
    def deposita(self, message):
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self):
        raise NotImplementedError

    