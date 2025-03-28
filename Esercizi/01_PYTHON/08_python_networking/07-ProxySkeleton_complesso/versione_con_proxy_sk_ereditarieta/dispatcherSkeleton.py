import socket, sys, time
from abc import ABC, abstractmethod
from dispatcher_service import DispatcherService
import multiprocess as mp



# process function
def run_function(conn, skeleton):

    # data received from client
    message = conn.recv(1024)
    print("MESSAGE received: ", message.decode('utf-8'))

    ## capisco se la richiesta è sendCmd o getCmd
    request = (message.decode('utf-8')).split('-')[0]
    print("[DispatcherSkeleton] request received: ", request)

    if request == "sendCmd" :
        value_to_send = (message.decode('utf-8')).split('-')[1]
        print("[DispatcherSkeleton] request is sendCmd, value is: ", value_to_send)
        skeleton.sendCmd(value_to_send) ### produzione sulla coda
        result = "ACK"
    else:
        print("[DispatcherSkeleton] request is getCmd...wait for result")
        result = skeleton.getCmd()
    
    print("[DispatcherSkeleton] result to send back: ", result)
    # send back reversed string to client
    conn.send(result.encode('utf-8'))

    # connection closed
    conn.close()
    
    
class DispatcherSkeleton(DispatcherService, ABC):
    """
    In questo caso, "attivo" l'ereditarietà, ovvero:
    - la classe Skeleton implementa Subject ed è una classe astratta
    - i metodi sono astratti lasciando l'implementazione a RealSubject che estende la classe astratta
    - la classe Skeleton NON utilizza un riferimento a Subject
    """

    def __init__(self, host, port):
        
        self.host = host
        self.port = port

    @abstractmethod
    def sendCmd(self, value):
        pass
    
    @abstractmethod
    def getCmd(self):
        pass
    
    # lo Skeleton implementa un server multiprocess che opera sulla Queue condivisa
    def run_skeleton(self):
        
        host = 'localhost'
        # q = mp.Queue(5)
        # create and bind a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        self.port = s.getsockname()[1] # get used port

        print("Socket binded to host: " + self.host + " and port: " + str(self.port))

        s.listen(30)
        print("Socket is listening")

        while True:

            # establish a connection with client
            c, addr = s.accept()
            print('Connected to :', addr[0], ':', addr[1])

            # start a new process
            t = mp.Process(target=run_function, args=(c, self))
            t.start()
            print("[DispatcherSkeleton] t is terminated")

        s.close()
        print("[DispatcherSkeleton] socket is closed...")

