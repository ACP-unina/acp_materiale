import socket, sys

def client(PORT):

	IP = 'localhost'
	BUFFER_SIZE = 1024
	MESSAGE = "Hello, World!\n"

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, PORT))
	s.send(MESSAGE.encode("utf-8"))

	data = s.recv(BUFFER_SIZE)
	print ("received data: " + data.decode("utf-8"))

	s.close()

if __name__ == "__main__":
	try:
		PORT = sys.argv[1]
	except IndexError:
		print("Please, specify PORT arg...")

	assert PORT != "", 'specify port'
	client(int(PORT))	
