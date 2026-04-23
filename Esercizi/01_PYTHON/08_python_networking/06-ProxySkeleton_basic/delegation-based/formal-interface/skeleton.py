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
class Skeleton(ServiceInterface):
    """
    In questo caso, "attivo" la delega, ovvero:
        - La classe Skeleton implementa l'interfaccia Subject e non è una classe astratta
        
        - Skeleton implementa Subject ma NON implementa esplicitamente il corpo della funzione request
            delegando l'implementazione e l'esecuzione a RealSubject

        - Utilizza un riferimento a chi implementa veramente Subject, ovvero RealSubject (vedi __init__ e self.subject)
    """

    def __init__(self, port, subject):
        self.port = port
        self.subject = subject

    # Il metodo request non è astratto, e delego l'esecuzione del metodo all'implementatore, RealSubject.
    def inverti_stringa(self, data):
        return self.subject.inverti_stringa(data)

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
