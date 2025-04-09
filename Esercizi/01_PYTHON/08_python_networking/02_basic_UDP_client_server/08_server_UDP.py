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

msgServer = "Ciao client!"
serverAddressPort = ("localhost", 0)  # Bind to any available port
bufferSize = 1024

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(serverAddressPort)

cur_port = s.getsockname()[1]
print("Server running on: localhost, port:", cur_port)

while True:  # Infinite loop to keep listening
    msgClient, addr = s.recvfrom(bufferSize)
    print("[Server]: Messaggio ricevuto: " + msgClient.decode("utf-8"))
    print("[Server]: Indirizzo client: {}".format(addr))

    print("[Server]: Invio dati al client")
    s.sendto(msgServer.encode("utf-8"), addr)
