from service_interface import IService
from abc import ABC, abstractmethod
import socket

import multiprocess as mp

# Process function
def proc_fun(c, service):

    # Receive the request
    data = c.recv(1024)

    # Chek the type of request and invoke the proper Service method
    # NOTE: the operator "in" is used, since Java adds extra characters when sending String over socket, which prevents the exact match
    if "preleva" in str(data.decode()) :

        result = service.preleva()

    else:

        id = str(data.decode()).split('-')[1]
        result = service.deposita(id)
    
    # Send the response
    # NOTE: It is required to add "\n" at the end of the String in order to allow Java application to receive the data
    string_to_send = (str(result)+"\n")
    c.send(string_to_send.encode())

    # Close connection
    c.close()


# Skeleton
class ServiceSkeleton(IService, ABC):

    def __init__(self, port, queue):
        self.port = port
        self.queue = queue

    @abstractmethod
    def deposita (self, valore):
        pass

    @abstractmethod
    def preleva(self):
        pass

    def run_skeleton(self):
        
        host = 'localhost'

        # Create and bind the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, self.port))

        s.listen(10) ## NOTA: quantificare il numero di richieste concorrenti in base a quelli inviate dal client

        print("Socket is listening")

        while True:

            # Establish a connection with client
            c, addr = s.accept()
            
            # Start a new process to serve the reqest
            p = mp.Process(target=proc_fun, args=(c, self))
            p.start()

        s.close()

