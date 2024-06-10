import sys
import grpc
import service_pb2_grpc
import service_pb2
import multiprocess as mp
import threading as thd
from concurrent import futures

QUEUE_SIZE = 5

# Service Implementation
class ServiceImpl(service_pb2_grpc.ServiceServicer):

    def __init__(self, queue, lock_d, lock_p, empty, full):
        self.queue = queue
        self.lock_d = lock_d
        self.lock_p = lock_p
        self.empty = empty
        self.full = full
    

    def deposita(self, request, context):
        
        self.empty.acquire() ### empty = 4 se sono il primo prod ad entrare

        with self.lock_d:
            self.queue.append([request.id, request.product])
        
        print("[SERVER-IMPL] Depositato [" + str(request.id) + ", " + request.product + "]")
        
        self.full.release() ## avviserò i consumatori che sono in attesa, che possono consumare

        return service_pb2.StringMessage(value="deposited")
    

    def preleva(self, request, context):

        self.full.acquire() ### full == -1 se entra per primo il consumatore
        
        with self.lock_p:
            result = self.queue.pop()
        print("[SERVER-IMPL] Prelevato [" + str(result[0]) + ", " + result[1] + "]")
        
        self.empty.release() ### andrò a risvegliare i prod. che sono in attesa

        return service_pb2.Item(id=result[0], product=result[1])

    def svuota(self, request, context):
        print("[SERVER-IMPL] Svuota")

        self.lock_d.acquire()
        self.lock_p.acquire()
        
        while not self.queue:
            result = self.queue.pop()
            print("[SERVER-IMPL] Prelevato [" + str(result[0]) + ", " + result[1] + "]")
        
            yield service_pb2.Item(id=result[0], product=result[1])

        self.lock_p.release()
        self.lock_d.release()


if __name__ == "__main__":

    # Create the Qeueue
    q = []
    lock_d = thd.Lock()
    lock_p = thd.Lock()
    empty = thd.Semaphore(QUEUE_SIZE) ### semaforo per la produzione, inizializzato a QUEUE_SIZE (N produttori possono produrre)
    full = thd.Semaphore(0) ### semaforo per la consumazione, inizializzato a 0 (NON POSSO CONSUMARE ALL'inizio)

    # Creating gRPC Server - NOTE:  options=(('grpc.so_reuseport', 0) allows raising an exception if a port is already used
    # WARNING: Scegliere opportunamente il numero di Worker, se infatti tutti i worker restano bloccati su chiamate bloccanti, 
    # il server non riuscirà a gestire altre richieste
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),)) 
    service_pb2_grpc.add_ServiceServicer_to_server(ServiceImpl(q, lock_d, lock_p, empty, full), server)

    port = 0 # with port = 0, the gRPC runtime will choose a port

    port = server.add_insecure_port('[::]:' + str(port)) 
    print('Starting server. Listening on port ' + str(port))

    server.start()

    print("Server running ... ")

    server.wait_for_termination()
