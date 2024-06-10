import socket

msgServer = "Ciao client!"
serverAddressPort = ("localhost".encode("utf-8"), 0)
bufferSize = 1024

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(serverAddressPort)

cur_port = s.getsockname()[1]

print("server on: localhost, port: ", cur_port)

msgClient, addr = s.recvfrom(bufferSize)
print("[Server]: Messaggio ricevuto: " + msgClient.decode("utf-8"))
print("[Server]: Indirizzo client: {}" .format(addr))

print ("[Server]: Invio dati al client")
s.sendto(msgServer.encode("utf-8"), addr)

s.close()

