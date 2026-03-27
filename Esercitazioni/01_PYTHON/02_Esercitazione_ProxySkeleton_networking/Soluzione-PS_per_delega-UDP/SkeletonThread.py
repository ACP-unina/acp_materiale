from threading import Thread, current_thread


class SkeletonThread(Thread):

    def __init__(self, sock, msgClient, addr, thd_name, ref):
        super().__init__(name=thd_name)
        self.sock = sock
        self.msgClient = msgClient
        self.addr = addr
        self.ref = ref

    def run(self):

        message = self.msgClient.decode('utf-8')
        print(f"[{current_thread().name}] Received: {message}")

        # Estraggo i parametri dalla richiesta, cioè metodo richiesto e l'articolo
        service = message.split('-')[0]
        articolo = message.split('-')[1]

        result = None

        # Verifico il metodo richiesto ed invoco il metodo corrispondente
        if service == "preleva":
            result = self.ref.preleva(articolo)

        elif service == "deposita":
            id_item = message.split('-')[2] # Nel caso di deposito estraggo anche l'id dalla richiesta
            result = self.ref.deposita(articolo, id_item)

        else:
            print(f"[{current_thread().name}] Servizio {service} non riconosciuto")
            

        # Invio la risposta al client, dopo averla trasformata in stringa
        response = str(result)
        self.sock.sendto(response.encode('utf-8'), self.addr)



