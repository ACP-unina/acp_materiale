from IMagazzino import IMagazzino

import socket


class MagazzinoProxy (IMagazzino):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.buf_size = 1024

        # Predispondo la socket UDP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def deposita(self, articolo, id_item):

        # Creo il messaggio prevedendo '-' come separatore
        # Ad esempio depostia-smartphone-10
        message_to_send = '-'.join(["deposita", articolo, str(id_item)])
        print("[MAGAZZINO PROXY] Sent request:", message_to_send)

        # Invio il messaggio ed attendo la risposta
        self.sock.sendto(message_to_send.encode("utf-8"), (self.ip, self.port))
        response, addr = self.sock.recvfrom(self.buf_size)

        print("[MAGAZZINO PROXY] Response:", response.decode("utf-8"))

        # Ritorno il risultato convertito come booleano
        return bool(response)


    def preleva(self, articolo):

        # Creo il messaggio prevedendo '-' come separatore
        # Ad esempio preleva-laptop
        message_to_send = '-'.join(["preleva", articolo])
        print("[MAGAZZINO PROXY] Sent request:", message_to_send)

        # Invio il messaggio ed attendo la risposta
        self.sock.sendto(message_to_send.encode("utf-8"), (self.ip, self.port))
        response, addr = self.sock.recvfrom(self.buf_size)

        response_message = response.decode("utf-8")

        print("[MAGAZZINO PROXY] Response:", response_message)

        # Ritorno il risultato convertito come intero
        return int(response_message)