import socket, sys, time
from abc import ABC, abstractmethod
from dispatcher_service import DispatcherService
import multiprocess as mp

# process function
def run_function(conn, skeleton):

    # data received from client
    message = conn.recv(1024)
    print("[DispatcherSkeleton run_function] MESSAGE received: ", message.decode('utf-8'))

    ## capisco se la richiesta è sendCmd o getCmd
    request = (message.decode('utf-8')).split('-')[0]
    print("[DispatcherSkeleton run_function] request received: ", request)

    if request == "sendCmd" :
        value_to_send = (message.decode('utf-8')).split('-')[1]
        print("[DispatcherSkeleton run_function] request is sendCmd, value is: ", value_to_send)
        skeleton.sendCmd(value_to_send) ### produzione sulla coda
        result = "ACK"
    else:
        print("[DispatcherSkeleton run_function] request is getCmd...wait for result")
        result = skeleton.getCmd()
    
    print("[DispatcherSkeleton run_function] result to send back: ", result)
    # send back reversed string to client
    conn.send(result.encode('utf-8'))

    # connection closed
    conn.close()
    
    
class DispatcherSkeleton(DispatcherService):
    
    """
    In questo caso, "attivo" la delega, ovvero:
        - La classe DispatcherSkeleton implementa l'interfaccia DispatcherService e non è una classe astratta
        
        - DispatcherSkeleton implementa DispatcherService ma NON implementa esplicitamente il corpo della funzione sendCmd
        e getCmd delegando l'implementazione e l'esecuzione a dispatcherImpl

        - Utilizza un riferimento a dispatcher_service che farà riferimento a sua volta a chi implementa veramente Subject, 
        ovvero dispatcherImpl (vedi __init__ e self.subject)
    """

    def __init__(self, host, port, dispatcher_service):
        
        self.host = host
        self.port = port
        self.dispatcher_service = dispatcher_service

    def sendCmd(self, value):
        #print("[DispatcherSkeleton sendCmd] ref to queue: ", self.dispatcher_service.queue)
        self.dispatcher_service.sendCmd(value)
    
    def getCmd(self):
        #print("[DispatcherSkeleton getCmd] ref to queue: ", self.dispatcher_service.queue)
        # ATTENZIONE: fare il return di getCmd() altrimenti si rompe tutto!!! far vedere!
        return self.dispatcher_service.getCmd()
    
    # lo Skeleton implementa un server multiprocess che opera sulla Queue condivisa
    def run_skeleton(self):
        
        host = 'localhost'
        
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

