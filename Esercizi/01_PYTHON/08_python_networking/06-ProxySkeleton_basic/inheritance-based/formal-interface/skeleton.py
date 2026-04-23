from abc import ABC, abstractmethod
from interface import ServiceInterface
import socket, sys, threading

# thread function
def thd_fun(c, self):


    # data received from client
    data = c.recv(1024)
    
    result = self.inverti_stringa(data)

    # send back reversed string to client
    c.send(result)

    # connection closed
    c.close()


# Il nostro server Skeleton
class Skeleton(ServiceInterface, ABC):
    """
    In questo caso, "attivo" l'ereditarietà, ovvero:
    - la classe Skeleton è una classe astratta (estendo ABC) e implementa ServiceInterface
    - i metodi sono astratti lasciando l'implementazione a ServiceImpl che estende la classe astratta
    - la classe Skeleton NON utilizza un riferimento a ServiceInterface
    """

    def __init__(self, port):
        self.port = port

    # metodo astratto che è implementato da chi estende lo Skeleton
    @abstractmethod
    def inverti_stringa(self, data):
        pass

    def run_skeleton(self):
        
        host = 'localhost'

        # create and bind a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, self.port))
        self.port = s.getsockname()[1] # get used port

        print("Socket binded to port", self.port)

        s.listen(5)
        print("Socket is listening")

        while True:

            # establish a connection with client
            c, addr = s.accept()
            print('Connected to :', addr[0], ':', addr[1])

            # start a new thread
            t = threading.Thread(target=thd_fun, args=(c, self))
            t.start()

        s.close()
