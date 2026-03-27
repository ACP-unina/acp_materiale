from concurrent import futures

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

### crea una classe Greeter che implementa il servizio GreeterServicer
### in questo caso implementiamo il metodo SayHello

class Greeter(helloworld_pb2_grpc.GreeterServicer):
	def SayHello(self, request, context):
		print("[server] SayHello method invoked, returning response...")
		return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

### implemento il metodo serve() che sarà invocato come prima funzione dal main

def serve():

	# mi istanzio un oggetto server da grpc
	# ALERT: i ThreadPool sono quelli del package concurrent e non multiprocess. Alcune diff in: https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	# aggiungo al server l'oggetto istanza del mio sercizio Greeter
	helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

	# faccio il bind con localhost al primo porto libero
	port = server.add_insecure_port("0.0.0.0:0")

	# avvio il server
	server.start()

	print("Server started, listening on " + str(port))

	# attendo che il server termini
	server.wait_for_termination()


if __name__ == "__main__":
	serve()
