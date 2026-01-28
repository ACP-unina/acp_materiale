from dispatcher_service import DispatcherService
import multiprocess as mq
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-0s)%(message)s',)

## implementazione di Subject
class dispatcherImpl(DispatcherService): # RealSubject estende Skeleton che implementa Subject (il mio servizio)

    def __init__(self, queue=mq.Queue(5)):
        self.queue = queue

    def sendCmd(self, value):
        #print(f'[dispatcherImpl sendCmd] ref to queue: {self.queue}')
        logging.info(f'[dispatcherImpl sendCmd] ref to queue: {self.queue}')
        self.queue.put(value)
    
    def getCmd(self):
        value_to_get = self.queue.get()
        #print(f'[dispatcherImpl getCmd] ref to queue: {self.queue} value get: {value_to_get}')
        logging.info(f'[dispatcherImpl getCmd] ref to queue: {self.queue} value get: {value_to_get}')
        return value_to_get
