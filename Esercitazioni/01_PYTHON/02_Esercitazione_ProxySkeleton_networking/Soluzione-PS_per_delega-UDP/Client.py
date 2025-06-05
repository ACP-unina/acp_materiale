from threading import Thread, current_thread
from MagazzinoProxy import MagazzinoProxy

import sys, random, time


def thread_fun(service, ip, port, num_reqs):

    # Genero il valore per l'attesa
    waiting_time = random.randint(2, 4)
    time.sleep(waiting_time)

    # Istanzio il Proxy
    proxy = MagazzinoProxy(ip, port)

    for i in range(num_reqs):
    
        # Genero in maniera casuale l'articolo
        choice = random.randint(0, 1)
        if choice == 0:
            articolo = "smartphone"
        else:
            articolo = "laptop"

        # Verifico il tipo di richiesta ed uso il proxy invocare il metodo corrispondente
        if service == "deposita":

            # Genero l'id casualmente
            id_item = random.randint(1, 100)

            print(f"[{current_thread().name}] Sending request {service}, {articolo}, {id_item}")

            # Utilizzo il proxy per effettuare un deposito
            result = proxy.deposita(articolo, id_item)

            # Check del valore di ritorno
            if not result:
                print(f"[{current_thread().name}] Request {service}, {articolo}, {id_item} failed!")
            else:
                print(f"[{current_thread().name}] Request {service}, {articolo}, {id_item} succeed!")
        
        elif service == "preleva":

            print(f"[{current_thread().name}] Sending request {service}, {articolo}")
            
            # Utilizzo il proxy per effettuare un prelievo
            result = proxy.preleva(articolo)

            # Check del valore di ritorno
            if result == -1:
                print(f"[{current_thread().name}] Request {service}, {articolo} failed!")
            else:
                print(f"[{current_thread().name}] Request {service}, {articolo} succeed. ID={str(result)}")


NUM_THREADS = 5
NUM_REQS_THREADS = 3
IP = 'localhost'

# Recupero il nome del servizio e la porta del server, forniti come parametri da terminale
try:
    service = sys.argv[1]
    port = int(sys.argv[2])

except IndexError:
    print("[CLIENT] Missing service name and/or server port parameter/s")
    sys.exit(-1)


# Avvio i thread
threads = []

for i in range(NUM_THREADS):

    t = Thread(target=thread_fun, args=(service, IP, port, NUM_REQS_THREADS), name="CLIENT THREAD-"+str(i))
    threads.append(t)
    t.start()


# Attendo la terminazione dei thread
for i in range(NUM_THREADS):

    threads.pop().join()