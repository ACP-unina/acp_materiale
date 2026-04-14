import threading
import time

def task():
    print("[THREAD] inizio lavoro lungo")
    time.sleep(5)
    print("[THREAD] fine")

start = time.time()

t = threading.Thread(target=task, daemon=True)  # cambia True/False
t.start()

print("[MAIN] finito subito")

end = time.time()
print("Durata main:", end - start)
