import socket

#sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
sniffer.bind(('', 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
while True:
    print(sniffer.recvfrom(4096))
