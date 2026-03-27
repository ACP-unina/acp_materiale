import socket, sys
  
try:
    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003)) # 0x0003 sta per ogni protocollo supportato

except socket.error as msg:
    print("Socket could not be created. Error Code : " + str(msg[0]) + " Message " + msg[1])
    sys.exit()

while True:
    print(s.recvfrom(4096))
