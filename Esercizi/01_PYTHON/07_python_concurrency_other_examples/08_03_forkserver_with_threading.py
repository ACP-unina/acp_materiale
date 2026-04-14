import multiprocessing as mp
import threading
import time
import os

def holder(lock):
    lock.acquire()
    print(f"[parent thread] pid={os.getpid()} acquired multiprocessing.Lock")
    time.sleep(5)
    lock.release()
    print(f"[parent thread] pid={os.getpid()} released multiprocessing.Lock")

def child_process(lock):
    print(f"[child_process] pid={os.getpid()} trying to acquire multiprocessing.Lock")
    lock.acquire()
    print(f"[child_process] pid={os.getpid()} acquired multiprocessing.Lock")
    lock.release()

if __name__ == "__main__":
    ctx = mp.get_context("forkserver")
    lock = ctx.Lock()

    t = threading.Thread(target=holder, name="holder", args=(lock,))
    t.start()

    time.sleep(0.5)   # let the thread grab the lock

    p = ctx.Process(target=child_process, args=(lock,))
    p.start()

    p.join()          # wait normally; child should continue after ~5 s
    t.join()