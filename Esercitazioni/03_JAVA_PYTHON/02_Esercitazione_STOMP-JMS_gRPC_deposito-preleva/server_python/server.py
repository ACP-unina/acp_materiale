from concurrent import futures

import grpc
import magazzino_pb2
import magazzino_pb2_grpc
from multiprocess import Queue


class Magazzino(magazzino_pb2_grpc.MagazzinoServicer):

	def __init__(self, queue):
		self.queue = queue

	def preleva(self, request, context):

		result = self.queue.get()
		print("[SERVER-IMPL] Prelevato", result)

		return magazzino_pb2.Articolo(valore=result)

	def deposita(self, request, context):

		self.queue.put(request.valore)
		print("[SERVER-IMPL] Depositato", request.valore)
        
		return magazzino_pb2.Empty()


### implemento il metodo serve() che sarà invocato come prima funzione dal main

def serve():

	# mi istanzio un oggetto server da grpc
	# ALERT: i ThreadPool sono quelli del package concurrent e non multiprocess. Alcune diff in: https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	# Creo la coda
	queue = Queue(5)

	# aggiungo al server l'oggetto istanza del mio servizio 
	magazzino_pb2_grpc.add_MagazzinoServicer_to_server(Magazzino(queue), server)

	# faccio il bind al porto impostato
	port = server.add_insecure_port("[::]:0")

	# avvio il server
	server.start()

	print("Server started, listening on " + str(port))

	# attendo che il server termini
	server.wait_for_termination()


if __name__ == "__main__":
	serve()
