from dispatcherSkeleton import DispatcherSkeleton
import multiprocess as mq
## implementazione di Subject
class dispatcherImpl(DispatcherSkeleton): # RealSubject estende Skeleton che implementa Subject (il mio servizio)

    def __init__(self, host, port, queue=mq.Queue(5)):
        super().__init__(host, port)
        self.queue = queue

    def sendCmd(self, value):
        self.queue.put(value)
    
    def getCmd(self):
        return self.queue.get()
