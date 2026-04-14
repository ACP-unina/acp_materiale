import time
import threading
import multiprocessing


N = 40_000_000


def cpu_task(n):
    x = 0
    for i in range(n):
        x += i * i
    return x


def run_single():
    start = time.perf_counter()
    cpu_task(N)
    elapsed = time.perf_counter() - start
    print(f"single thread: {elapsed:.2f}s")


def run_threads(n):
    p_list = []
    start = time.perf_counter()

    for i in range(n):
        p = threading.Thread(target=cpu_task, args=(N // n,))
        p_list.append(p)
    
    for p in p_list:
        p.start()
    
    for p in p_list:
        p.join()

    elapsed = time.perf_counter() - start
    print(f"{n} threads:     {elapsed:.2f}s")


def run_processes(n):
    p_list = []
    start = time.perf_counter()

    for i in range(n):
        p = multiprocessing.Process(target=cpu_task, args=(N // n,))
        p_list.append(p)
    
    for p in p_list:
        p.start()
    
    for p in p_list:
        p.join()
   
    elapsed = time.perf_counter() - start
    print(f"{n} processes:   {elapsed:.2f}s")


if __name__ == "__main__":
    run_single()
    run_threads(8)
    run_processes(8)
