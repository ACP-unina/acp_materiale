from MagazzinoSkeleton import MagazzinoSkeleton
from threading import Lock, Condition



class MagazzinoImpl(MagazzinoSkeleton):

    def __init__(self, ip, port, queue_size = 5):
        super().__init__(ip, port)
        
        self.laptop_queue = []
        self.smartphone_queue = []
        
        self.queue_size = queue_size

        cv_laptop_lock = Lock()
        self.laptop_producer_cv = Condition(lock=cv_laptop_lock)
        self.laptop_consumer_cv = Condition(lock=cv_laptop_lock)

        cv_smartphone_lock = Lock()
        self.smartphone_producer_cv = Condition(lock=cv_smartphone_lock)
        self.smartphone_consumer_cv = Condition(lock=cv_smartphone_lock)

        self.laptop_file_name = "laptop.txt"
        self.smartphone_file_name = "smartphone.txt"

        laptop_file = open(self.laptop_file_name, 'a')
        laptop_file.truncate(0)

        smartphone_file = open(self.smartphone_file_name, 'a')
        smartphone_file.truncate(0)

    def deposita(self, articolo, id_item):
        
        success = True

        # Verifico il tipo di articolo ed effettuo l'operazione di deposito sulla coda corrispondente
        if articolo == "laptop":

            # Acquisisco il lock 
            with self.laptop_producer_cv:

                # Verifico che ci sia spazio
                while not self.a_space_is_available(self.laptop_queue):
                    self.laptop_producer_cv.wait()

                # Deposito un laptop
                id_item = self.laptop_queue.append(id_item)

                # Notifico i consumatori
                self.laptop_consumer_cv.notify()

        elif articolo == "smartphone":

            # Acquisisco il lock 
            with self.smartphone_producer_cv:

                # Verifico che ci sia spazio
                while not self.a_space_is_available(self.smartphone_queue):
                    self.smartphone_producer_cv.wait()

                # Deposito un laptop
                id_item = self.smartphone_queue.append(id_item)

                # Notifico i consumatori
                self.smartphone_consumer_cv.notify()

        else:
            print("[MAGAZZINO IMPL] Articolo non riconosciuto")
            success = False

        
        return success



    def preleva(self, articolo):
        
        id_item = -1

        # Verifico il tipo di articolo ed effettuo l'operazione di prelievo sulla coda corrispondente
        if articolo == "laptop":

            # Acquisisco il lock 
            with self.laptop_consumer_cv:

                # Verifico che ci sia spazio
                while not self.an_item_is_available(self.laptop_queue):
                    self.laptop_consumer_cv.wait()

                # Prelevo un laptop
                id_item = self.laptop_queue.pop(0)

                with open(self.laptop_file_name, 'a') as file:
                    file.write(str(id_item)+"\n")

                # Notifico i produttori
                self.laptop_producer_cv.notify()

        elif articolo == "smartphone":

            # Acquisisco il lock 
            with self.smartphone_consumer_cv:

                # Verifico che ci sia spazio
                while not self.an_item_is_available(self.smartphone_queue):
                    self.smartphone_consumer_cv.wait()

                # Prelevo un laptop
                id_item = self.smartphone_queue.pop(0)

                with open(self.smartphone_file_name, 'a') as file:
                    file.write(str(id_item)+"\n")

                # Notifico i produttori
                self.smartphone_producer_cv.notify()

        else:
            print("[MAGAZZINO IMPL] Articolo non riconosciuto")

        
        return id_item


    def an_item_is_available(self, queue):
        return not (len(queue) == 0)

    def a_space_is_available(self, queue):
        return not (len(queue) == self.queue_size)