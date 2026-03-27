from IMagazzino import IMagazzino
from threading import Lock, Condition


class MagazzinoImpl(IMagazzino):

    def __init__(self, queue_size = 5):
        
        # Inizializzo le code
        self.laptop_queue = []
        self.smartphone_queue = []
        
        self.queue_size = queue_size

        # Instanzio lock e variabili condition per gestire le due code con prod-cons
        cv_laptop_lock = Lock()
        self.laptop_producer_cv = Condition(lock=cv_laptop_lock)
        self.laptop_consumer_cv = Condition(lock=cv_laptop_lock)

        cv_smartphone_lock = Lock()
        self.smartphone_producer_cv = Condition(lock=cv_smartphone_lock)
        self.smartphone_consumer_cv = Condition(lock=cv_smartphone_lock)

        self.laptop_file_name = "laptop.txt"
        self.smartphone_file_name = "smartphone.txt"

        # Svuoto i file 
        laptop_file = open(self.laptop_file_name, 'a')
        laptop_file.truncate(0)
        laptop_file.close()

        smartphone_file = open(self.smartphone_file_name, 'a')
        smartphone_file.truncate(0)
        smartphone_file.close()


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
                self.laptop_queue.append(id_item)
                print(f"[MAGAZZINO IMPL] Added {id_item} in {articolo}")

                # Notifico i consumatori
                self.laptop_consumer_cv.notify()

        elif articolo == "smartphone":

            # Acquisisco il lock 
            with self.smartphone_producer_cv:

                # Verifico che ci sia spazio
                while not self.a_space_is_available(self.smartphone_queue):
                    self.smartphone_producer_cv.wait()

                # Deposito un laptop
                self.smartphone_queue.append(id_item)
                print(f"[MAGAZZINO IMPL] Added {id_item} in {articolo}")

                # Notifico i consumatori
                self.smartphone_consumer_cv.notify()

        else:
            print("[MAGAZZINO IMPL] Article not recognized")
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
                print(f"[MAGAZZINO IMPL] Got {id_item} from {articolo}")

                # Scrivo l'id prelevato sul file dei laptop
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
                print(f"[MAGAZZINO IMPL] Got {id_item} from {articolo}")

                # Scrivo l'id prelevato sul file degli smartphone
                with open(self.smartphone_file_name, 'a') as file:
                    file.write(str(id_item)+"\n")

                # Notifico i produttori
                self.smartphone_producer_cv.notify()

        else:
            print("[MAGAZZINO IMPL] Article not recognized")

        
        return id_item


    # Metodi di utilità per la verifica delle condizioni prod-cons

    def an_item_is_available(self, queue):
        return not (len(queue) == 0)

    def a_space_is_available(self, queue):
        return not (len(queue) == self.queue_size)