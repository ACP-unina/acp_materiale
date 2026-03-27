from abc import ABC, abstractmethod


class IMagazzino(ABC):

    @abstractmethod
    def deposita(self, articolo, id_item):
        pass

    @abstractmethod
    def preleva(self, articolo):
        pass