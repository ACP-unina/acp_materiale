from IMagazzino import IMagazzino

import socket

class MagazzinoProxy (IMagazzino):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.buf_size = 1024

    def deposita(self, articolo, id):
        
        # Predispondo la socket TCP e rchiedo la connessione al server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))

        # Creo il messaggio prevedendo '-' come separatore
        # Ad esempio depostia-smartphone-10
        message_to_send = '-'.join(["deposita", articolo, str(id)])
        print("[MAGAZZINO PROXY] Sent request:", message_to_send)

        # Invio il messaggio ed attendo la risposta
        sock.send(message_to_send.encode("utf-8"))
        response = sock.recv(self.buf_size)

        print("[MAGAZZINO PROXY] Response:", response.decode("utf-8"))

        # Ritorno il risultato convertito come booleano
        return bool(response)



    def preleva(self, articolo):
        
        # Predispondo la socket TCP e rchiedo la connessione al server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))

        # Creo il messaggio prevedendo '-' come separatore
        # Ad esempio preleva-laptop
        message_to_send = '-'.join(["preleva", articolo])
        print("[MAGAZZINO PROXY] Sent request:", message_to_send)

        # Invio il messaggio ed attendo la risposta
        sock.send(message_to_send.encode("utf-8"))
        response = sock.recv(self.buf_size)

        response_message = response.decode("utf-8")

        print("[MAGAZZINO PROXY] Response:", response_message)

        # Ritorno il risultato convertito come intero
        return int(response_message)