import sys
import threading as mt
import random
from dispatcher_proxy import DispatcherProxy


N_CLIENTS = 5
N_reqs_per_client = 3

def generate_client_reqs(host, port):
    
        for i in range(N_reqs_per_client):
    
            value_to_deposit = random.randint(0,3) #tra 0-leggi, 1-scrivi, 2-configura, 3-reset. Ciascun thread effettua 3 richieste.

            ## istanzio un proxy lato client e invoco sendCmd
            thread_name = mt.current_thread().name

            proxy = DispatcherProxy(host, int(port), thread_name, i)
            proxy.sendCmd(value_to_deposit)


if __name__ == "__main__":

    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("Please, specify HOST/PORT args...")
        sys.exit(-1)

    # Make the requests
    clients = []
    for i in range (N_CLIENTS):

        # creazione del process con callable object (func)
        cli = mt.Thread(target=generate_client_reqs, args=(HOST, PORT))

        cli.start()

        clients.append(cli)    

    
    # waiting consumers termination
    for i in range (N_CLIENTS):

        clients[i].join()