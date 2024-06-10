from abc import ABC, abstractmethod
from interface import Subject
import socket, sys
import threading

# thread function
def thd_fun(c, self):


    # data received from client
    data = c.recv(1024)

    result = self.request(data)
    
    # send back reversed string to client
    c.send(result)

    # connection closed
    c.close()

# Il nostro server Skeleton
class Skeleton(Subject, ABC):
    """
    In questo caso, "attivo" l'ereditarietà, ovvero:
    - la classe Skeleton implementa Subject ed è una classe astratta
    - i metodi sono astratti lasciando l'implementazione a RealSubject che estende la classe astratta
    - la classe Skeleton NON utilizza un riferimento a Subject
    """

    def __init__(self, port):
        self.port = port

    # metodo astratto che è implementato da chi estende lo Skeleton
    @abstractmethod
    def request(self, data):
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


## implementazione di Subject
class RealSubject(Skeleton): # RealSubject estende Skeleton che implementa Subject (il mio servizio)
    
    def request(self, data):
        # reverse the given string from client
        data = data[::-1]

        return data


if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")
    
    print("Server running")

    """
    Quando uso lo Skeleton per ereditarietà, lato business logic devo:
        - istanziare un oggetto RealSubject che estende lo Skeleton
        - far partire lo skeleton con l'istanza di RealSubject che ho appena creato
    """

    realSubject = RealSubject(int(PORT))
    realSubject.run_skeleton()
