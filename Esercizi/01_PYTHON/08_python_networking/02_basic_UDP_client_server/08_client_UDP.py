import socket, sys

def client(port):
	
	msgClient = "Ciao server!"
	serverAddressPort = ("localhost".encode("utf-8"), port)
	bufferSize = 1024

	s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	print ("[Client]: Invio dati al server. msg: ", msgClient)
	s.sendto(msgClient.encode("utf-8"), serverAddressPort)

	msgServer, addr = s.recvfrom(bufferSize)
	print("[Client]: Risposta server: " + msgServer.decode("utf-8"))

	s.close()


if __name__ == "__main__":
    try:
        port = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg...")

    assert port != "", 'specify port'
    client(int(port))

