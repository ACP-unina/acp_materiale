import multiprocessing as mp
import threading
import time
import os

def holder():
    lock.acquire()
    print(f"[parent thread] pid={os.getpid()} acquired threading.Lock")
    time.sleep(5)   # keep it locked
    lock.release()
    print(f"[parent thread] pid={os.getpid()} released threading.Lock")

def child_process():
    print(f"[child_process] pid={os.getpid()} trying to acquire threading.Lock")
    lock.acquire()
    print(f"[child_process] pid={os.getpid()} acquired threading.Lock")  # likely never printed
    lock.release()

if __name__ == "__main__":
    mp.set_start_method("fork")

    """
    NOTA: threading.Lock() è un lock che non è pensato per essere condiviso tra più processi, ma solo
    tra più thread!
    """
    lock = threading.Lock() 
    
    t = threading.Thread(target=holder, name="holder")
    t.start()

    time.sleep(0.5)   # let the thread grab the lock

    p = mp.Process(target=child_process) 
    p.start()

    """
    da questo momento in poi il processo padre crea un figlio con fork.
    il figlio eredità tutto del padre, incluso lo stato dell'oggetto lock che 
    un thread ha acquisito. Ovviamente dopo la fork, soltanto il current thread (che è il MainThread) 
    sarà attivo, mentre l'altro thread holder non ESISTERA'.
    In questo caso child_process proverà ad acquisire l'ogetto lock che non sarà mai rilasciato dal thread
    holder!!!
    """

    p.join(timeout=2) 

    if p.is_alive(): 
        """
        il processo padre attende p con un timeout, e questo timeout sicuramente scadrà, quindi faccio il check
        con is_alive() che ritornerà True
        """
        print("[main] child_process is stuck: inherited locked threading.Lock")
        p.terminate()
        p.join()

    t.join()
