import multiprocessing as mp
import threading
import time
import os


def holder():
    lock.acquire()
    print(f"[parent thread] pid={os.getpid()} acquired multiprocessing.Lock")
    time.sleep(5)
    lock.release()
    print(f"[parent thread] pid={os.getpid()} released multiprocessing.Lock")

def child_process():
    print(f"[child] pid={os.getpid()} trying to acquire multiprocessing.Lock")
    with lock:
        print(f"[child] pid={os.getpid()} acquired multiprocessing.Lock")

if __name__ == "__main__":
    #mp.get_context("fork")
    mp.set_start_method("fork")
    
    lock = mp.Lock()
    
    t = threading.Thread(target=holder)
    t.start()

    time.sleep(0.5)   # let the parent thread acquire the lock first

    p = mp.Process(target=child_process)
    p.start()

    """
    NOTA: multiprocessing.Lock() è un lock che è pensato per essere CONDIVISO tra più processi!
    Questo significa che, nonostante io abbia usato la fork, e nel processo figlio solo il current thread
    (MainThread) è attivo, prima o poi il thread holder (che non esisterà più nel contesto del processo figlio p)
    rilascerà tale lock che è condiviso però con il processo figlio p. In questa soluzione quindi il processo 
    child_process non rimarrà in deadlock.
    """

    p.join(timeout=2)

    if p.is_alive():
        """
        il processo padre attende p con un timeout, e questo timeout sicuramente scadrà, quindi faccio il check
        con is_alive() che ritornerà True
        """
        print("[main] child_process is still waiting, not deadlocked yet")
        p.join()   # wait until the parent thread releases the lock

    t.join()
