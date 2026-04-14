#### ESERCIZIO PROD_CONS con variabili condition

import logging
import multiprocessing
import time
from random import randint

CONSUMER = 'Consumer-'
PRODUCER = 'Producer-'
N_CONSUMERS = 10
N_PRODUCERS = 10
QUEUE_SIZE = 5

logging.basicConfig(level=logging.DEBUG, format='[%(processName)-0s] %(message)s',)

class consumerProcess(multiprocessing.Process):
    
    def __init__(self, queue, name):

        multiprocessing.Process.__init__(self, name=name)
        self.queue = queue

    def run(self):
        logging.debug('\t\t\tStarted')

        item = self.queue.get()
        logging.debug('\t\t\tConsumed Item: %r', item)


def produce_one_item(queue):
    logging.debug('Started')
    
    item = randint(0, 100)
    queue.put(item)
    logging.debug('Produced Item: %r', item)


def main():
    
    # generating the queue 
    queue = multiprocessing.Queue(QUEUE_SIZE) ### multiprocessing.Queue is prcess/thread-safe

    consumers = []
    producers = []

    # generating the consumers
    for i in range (N_CONSUMERS):
        
        name=CONSUMER+str(i)

        ct = consumerProcess(queue, name)
        ct.start()

        consumers.append(ct)


    # generating the producers
    for i in range (N_PRODUCERS):

        pt = multiprocessing.Process(
            target=produce_one_item,
            name=PRODUCER+str(i),
            args=(queue,),
        )

        pt.start()

        producers.append(pt)

    
    # waiting consumers termination
    for consumer in consumers:
        consumer.join()


    # waiting producers termination
    for producer in producers:
        producer.join()



if __name__ == '__main__':
    main()

