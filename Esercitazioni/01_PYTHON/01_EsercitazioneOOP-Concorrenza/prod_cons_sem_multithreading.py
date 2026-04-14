#### ESERCIZIO PROD_CONS con SEMAFORI con MULTITHREADING

import logging
import threading
import time
from random import randint

CONSUMER = 'Consumer'
PRODUCER = 'Producer'
N_CONSUMERS = 10
N_PRODUCERS = 10
QUEUE_SIZE = 5

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-0s] %(message)s',)

def get_an_available_item(queue):
    return queue.pop(0)


def make_an_item_available(queue):
    item = randint(0, 100)
    queue.append(item)

    return item


class consumerThread(threading.Thread):
    
    def __init__(self, mutex_C, empty, full, queue, name):

        threading.Thread.__init__(self, name=name)
        self.mutex_C = mutex_C
        self.empty = empty
        self.full = full
        self.queue = queue

    def run(self):
        logging.debug('\t\t\tStarted')

        logging.debug('\t\t\tChecking full semaphore ...')

        ####
        self.full.acquire() ### full == -1 se entra per primo il consumatore

        ### mutex.acquire()
        with self.mutex_C: ### entrerò se mutex>=0, lockare il mutex prima dell'acquire di empty è un errore perchè non consentiamo consumazioni di elementi consumabili
            
            logging.debug('\t\t\tAcquired mutex')
        
            time.sleep(1.0)
            item = get_an_available_item(self.queue)
            logging.debug('\t\t\tItem: %r', item)

            logging.debug('\t\t\tRelease mutex')
            
        ## mutex.release()
            
        self.empty.release() ### andrò a risvegliare i prod. che sono in attesa
        
        logging.debug('\t\t\tReleased empty semaphore')

def produce_one_item(mutex_P, empty, full, queue):
    logging.debug('Started')

    logging.debug('Checking empty semaphore...')

    empty.acquire() ### empty = 4 se sono il primo prod ad entrare

    with mutex_P: # lockare il mutex prima dell'acquire di empty è un errore perchè non consentiamo produzione di elementi producibili
        logging.debug('Acquired mutex')

        time.sleep(1.0)
        item = make_an_item_available(queue)
        logging.debug('Item: %r', item)


        logging.debug('Release mutex')
        
    full.release() ## avviserò i consumatori che sono in attesa, che possono consumare

    logging.debug('Released full semaphore')


def main():
    
    # generating the queue, coda fatta con una list
    queue = [] 

    # Creiamo i semafori per gestire il problem prod/cons multipli
    mutex_P = threading.Semaphore() ### = 1 mutua esclusione tra i diversi prod durante la produzione
    mutex_C = threading.Semaphore() ### = 1 mutua esclusione tra i diversi cons durante la consumazione
    
    empty = threading.Semaphore(QUEUE_SIZE) ### semaforo per la produzione, inizializzato a QUEUE_SIZE (N produttori possono produrre)
    full = threading.Semaphore(0) ### semaforo per la consumazione, inizializzato a 0 (NON POSSO CONSUMARE ALL'inizio)

    consumers = []
    producers = []

    # generating the consumers
    for i in range (N_CONSUMERS):
        
        name=CONSUMER+str(i)

        # creazione del thread con estensione della classe Thread
        ct = consumerThread(mutex_C, empty, full, queue, name)
        ct.start()

        consumers.append(ct)


    # generating the producers
    for i in range (N_PRODUCERS):

        # creazione del thread con callable object (func)
        pt = threading.Thread(target=produce_one_item, name=PRODUCER+str(i),
                                args=(mutex_P, empty, full, queue),)

        pt.start()

        producers.append(pt)

    
    # waiting consumers termination
    for i in range (N_CONSUMERS):

        consumers[i].join()


    # waiting producers termination
    for i in range (N_PRODUCERS):

        producers[i].join()



if __name__ == '__main__':
    main()
