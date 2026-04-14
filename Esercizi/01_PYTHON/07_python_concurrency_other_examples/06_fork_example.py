import multiprocessing, os
from multiprocessing import Process, Lock

multiprocessing.set_start_method("fork")

print(f'[GLOBAL] process id: {os.getpid()} __name__: {__name__}')


def run_function(x):
	PID = os.getpid()
	print(f'process id: {PID} __name__: {__name__}')
	print("x =", x)
	print(f"process id: {PID} l1 = {hex(id(l1))}")
	l1.acquire()
	print(f"process id: {PID} sez. critica figlio...")
	l1.release()

if __name__== "__main__":

	PID = os.getpid()
	l1 = Lock()

	print(f"process id: {PID} l1 = {hex(id(l1))}")

	p = Process(target=run_function, args=(10,))
	p.start()
	
	l1.acquire()
	print("sez. critica padre...")
	l1.release()
	p.join()
