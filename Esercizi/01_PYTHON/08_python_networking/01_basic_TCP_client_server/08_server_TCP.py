"""
# emulazione network delay in un sistema Linux
sudo apt update && sudo apt install iproute2 -y 

## add delay on loopback
sudo tc qdisc add dev lo root netem delay 1000ms

## add corruption of 10% of traffic on loopback
sudo tc qdisc add dev lo root netem corrupt 10%

## add drop of 20% of traffic on loopback
sudo tc qdisc add dev lo root netem drop 10%

## remove delay on loopback
sudo tc qdisc del dev lo root

## list tc rules
sudo tc qdisc show
"""

import socket

IP = '0.0.0.0'
PORT = 0
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)

cur_port = s.getsockname()[1]

print("server on: ", IP, "port: ", cur_port)

while True:
    conn, addr = s.accept()
    print("client addr: " + str(addr))
    print  ('Connection address: {}' .format(addr))
    toClient= "The world never says hello back!\n"

    data = conn.recv(BUFFER_SIZE)
    print ("received data: " + data.decode("utf-8"))

    conn.send(toClient.encode("utf-8"))

    conn.close()

s.close()
