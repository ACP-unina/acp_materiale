import socket

IP = '0.0.0.0'
PORT = 0
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)

cur_port = s.getsockname()[1]

print("server on: ", IP, "port: ", cur_port)

conn, addr = s.accept()
print("client addr: " + str(addr))
print  ('Connection address: {}' .format(addr))
toClient= "The world never says hello back!\n"

data = conn.recv(BUFFER_SIZE)
print ("received data: " + data.decode("utf-8"))

conn.send(toClient.encode("utf-8"))

conn.close()
s.close()
