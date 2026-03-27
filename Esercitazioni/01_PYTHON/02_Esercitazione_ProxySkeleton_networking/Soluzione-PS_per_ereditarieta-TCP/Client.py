from threading import Thread, current_thread
from MagazzinoProxy import MagazzinoProxy

import sys
import random
import time


def thread_fun(service, ip, port, num_reqs):

    # Genero il valore per l'attesa
    waiting_time = random.randint(2, 4)
    time.sleep(waiting_time)

    proxy = MagazzinoProxy(ip, port)

    for i in range(num_reqs):
    
        choice = random.randint(0, 1)

        if choice == 0:
            articolo = "smartphone"
        else:
            articolo = "laptop"

        if service == "deposita":
            id = random.randint(1, 100)
            print(f"[{current_thread().name}] Sending request {service}, {articolo}, {id}")
            result = proxy.deposita(articolo, id)

            if not result:
                print(f"[{current_thread().name}] Request failed!")
            else:
                print(f"[{current_thread().name}] Request succeed!")
        
        elif service == "preleva":
            print(f"[{current_thread().name}] Sending request {service}, {articolo}")
            result = proxy.preleva(articolo)

            if result == -1:
                print(f"[{current_thread().name}] Request failed!")
            else:
                print(f"[{current_thread().name}] Response succeed. ID={str(result)}")


NUM_THREADS = 5
NUM_REQS_THREADS = 3
IP = 'localhost'

# Recupero il nome del servizio fornito come parametro
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