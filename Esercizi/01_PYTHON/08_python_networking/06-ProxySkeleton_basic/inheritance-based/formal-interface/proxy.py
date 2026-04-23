from interface import ServiceInterface
import socket, sys

class Proxy(ServiceInterface):
    
    def __init__(self, port):
        self.port = port

    def inverti_stringa(self, message):

        IP = 'localhost'
        BUFFER_SIZE = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, self.port))
        s.send(message.encode("utf-8")) #manda la richiesta su socket del messaggio da invertire

        data = s.recv(BUFFER_SIZE) #ricevi il messaggio invertito

        s.close()

        return data
