from abc import ABC, abstractmethod

class DispatcherService(ABC):

    @abstractmethod
    def sendCmd(self, value):
        raise NotImplementedError
    
    @abstractmethod
    def getCmd(self):
        raise NotImplementedError