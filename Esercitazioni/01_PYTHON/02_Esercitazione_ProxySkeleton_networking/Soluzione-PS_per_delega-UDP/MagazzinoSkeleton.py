from IMagazzino import IMagazzino
from SkeletonThread import SkeletonThread

import socket


class MagazzinoSkeleton(IMagazzino):

    def __init__(self, ip, port, delegate):
        self.ip = ip
        self.port = port
        self.buf_size = 1024
        self.delegate = delegate

    def deposita(self, articolo, id_item):
        return self.delegate.deposita(articolo, id_item)

    def preleva(self, articolo):
        return self.delegate.preleva(articolo)

    def runSkeleton(self):
        
        # Predispongo socket UDP per la comunicazione con i client
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip, self.port))

        print("[MAGAZZINO SKELETON] Ready on port:", sock.getsockname()[1])
        
        i = 0

        while True:

            # Attesa richiesta
            msgClient, addr = sock.recvfrom(self.buf_size)

            i = i + 1

            # Avvio un Thread per la gestione della richiesta
            thread = SkeletonThread(sock, msgClient, addr, "SKELETON THREAD-"+str(i), self)
            thread.start()


        sock.close()

