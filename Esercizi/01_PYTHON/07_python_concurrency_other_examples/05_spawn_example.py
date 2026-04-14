import multiprocessing, os, time
from multiprocessing import Process, Lock

print(f'[GLOBAL] process id: {os.getpid()} __name__: {__name__}')


def run_function(x):
	print(f'process id: {os.getpid()} __name__: {__name__}')
	print("x =", x)
	print(f'PID: {os.getpid()} l: {hex(id(l))}')
	print(f'PID: {os.getpid()} WAITING TO ENTER SEZ. CRITICA')
	with l:
		print(f'PID: {os.getpid()} in sez. critica')

if __name__ == "__main__": ## Prova a togliere questo check, con spawn non è possibile 
	multiprocessing.set_start_method("spawn")

	l = Lock()
	print(f'PID: {os.getpid()} l: {hex(id(l))}')
	#p = Process(target=run_function, args=(10,l))
	p = Process(target=run_function, args=(10,))
	p.start()
	
	time.sleep(2)
	l.acquire()
	print(f'PID: {os.getpid()} in sez. critica')
	l.release()
	
	p.join()
