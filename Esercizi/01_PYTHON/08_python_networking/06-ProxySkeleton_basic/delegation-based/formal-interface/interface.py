from abc import ABC, abstractmethod

# La mia applicazione fornisce un servizio di inversion stringa tramite il metodo inverti_stringa
class ServiceInterface(ABC):

    @abstractmethod
    def inverti_stringa(self, data):
        pass