from interface import Subject
import socket, sys

class Proxy(Subject):
    
    def __init__(self, port):
        self.port = port

    def request(self, message):

        IP = 'localhost'
        BUFFER_SIZE = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, self.port))
        s.send(message.encode("utf-8"))

        data = s.recv(BUFFER_SIZE)
        print ("received data: " + data.decode("utf-8"))

        s.close()
