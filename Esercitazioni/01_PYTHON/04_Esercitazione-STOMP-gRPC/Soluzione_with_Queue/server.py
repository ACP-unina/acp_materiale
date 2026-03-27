import sys
import grpc
import service_pb2_grpc
import service_pb2
import multiprocess as mp
from concurrent import futures



# Service Implementation
class ServiceImpl(service_pb2_grpc.ServiceServicer):

    def __init__(self, queue, lock_d, lock_p):
        self.queue = queue
        self.lock_d = lock_d
        self.lock_p = lock_p
    

    def deposita(self, request, context):
        
        with self.lock_d:
            self.queue.put([request.id, request.product])
        
        print("[SERVER-IMPL] Depositato [" + str(request.id) + ", " + request.product + "]")
        
        return service_pb2.StringMessage(value="deposited")
    

    def preleva(self, request, context):

        with self.lock_p:
            result = self.queue.get()
        print("[SERVER-IMPL] Prelevato [" + str(result[0]) + ", " + result[1] + "]")
        
        return service_pb2.Item(id=result[0], product=result[1])

    def svuota(self, request, context):
        print("[SERVER-IMPL] Svuota")

        self.lock_d.acquire()
        self.lock_p.acquire()
        
        while not self.queue.empty():
            result = self.queue.get()
            print("[SERVER-IMPL] Prelevato [" + str(result[0]) + ", " + result[1] + "]")
        
            yield service_pb2.Item(id=result[0], product=result[1])

        self.lock_p.release()
        self.lock_d.release()


if __name__ == "__main__":

    # Create the Qeueue
    q = mp.Queue(5)
    lock_d = mp.Lock()
    lock_p = mp.Lock()

    # Creating gRPC Server - NOTE:  options=(('grpc.so_reuseport', 0) allows raising an exception if a port is already used
    # WARNING: Scegliere opportunamente il numero di Worker, se infatti tutti i worker restano bloccati su chiamate bloccanti, 
    # il server non riuscirà a gestire altre richieste
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),)) 
    service_pb2_grpc.add_ServiceServicer_to_server(ServiceImpl(q, lock_d, lock_p), server)

    port = 0 # with port = 0, the gRPC runtime will choose a port

    port = server.add_insecure_port('[::]:' + str(port)) 
    print('Starting server. Listening on port ' + str(port))

    server.start()

    print("Server running ... ")

    server.wait_for_termination()
