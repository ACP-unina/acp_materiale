from threading import Thread, current_thread

class SkeletonThread(Thread):

    def __init__(self, conn, buf_size, thd_name, ref):
        super().__init__(name=thd_name)
        self.conn = conn
        self.ref = ref
        self.buf_size = buf_size

    def run(self):
        
        # Ricevo la richiesta e decodifico il messaggio
        data = self.conn.recv(self.buf_size)
        message = data.decode('utf-8')

        print(f"[{current_thread().name}] Received: {data.decode('utf-8')}")

        # Estraggo i parametri dalla richiesta, cioè metodo richiesto e l'articolo
        service = message.split('-')[0]
        articolo = message.split('-')[1]

        result = None

        # Verifico il metodo richiesto ed invoco il metodo corrispondente
        if service == "preleva":
            result = self.ref.preleva(articolo)

        elif service == "deposita":
            id = message.split('-')[2] # Nel caso di deposito estraggo anche l'id dalla richiesta
            result = self.ref.deposita(articolo, id)

        else:
            print(f"[{current_thread().name}] Servizio {service} non riconosciuto")
            

        # Invio la risposta al client, dopo averla trasformata in stringa
        response = str(result)
        self.conn.send(response.encode('utf-8'))

        self.conn.close()


