from interface import Service
import socket, sys
import multiprocess as mp

# Process function
def proc_fun(c, service):

    # Receive the request
    data = c.recv(1024)

    # Chek the tyope of request and invoke the proper Service method
    if str(data.decode()) == "preleva" :

        result = service.preleva()

    else:

        id = str(data.decode()).split('-')[1]
        result = service.deposita(id)
    
    # Send the response
    c.send(str(result).encode())

    # Close connection
    c.close()

# Skeleton
class ServiceSkeleton(Service):

    def __init__(self, port, queue):
        self.port = port
        self.queue = queue

    def deposita (self, id):
        pass

    def preleva(self):
        pass

    def run_skeleton(self):
        
        host = 'localhost'

        # Create and bind the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, self.port))

        s.listen(5)
        print("Socket is listening")

        while True:

            # Establish a connection with client
            c, addr = s.accept()

            # Start a new process to serve the reqest
            p = mp.Process(target=proc_fun, args=(c, self))
            p.start()

        s.close()

# Service Implementation
class ServiceImpl(ServiceSkeleton):
    
    def deposita(self, data):

        self.queue.put(data)
        print("[SERVER-IMPL] Depositato", data)
        
        return "deposited"
    
    def preleva(self):

        result = self.queue.get()
        print("[SERVER-IMPL] Prelevato", result)
        
        return result


if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")
    
    print("Server running ... ")

    # Create the Qeueue
    q = mp.Queue(5)

    # Create the Service and run the Skeleton
    serviceImpl = ServiceImpl(int(PORT), q)
    serviceImpl.run_skeleton()
