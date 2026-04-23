from abc import ABC, abstractmethod
from serviceImpl import ServiceImpl
from skeleton import Skeleton
import threading, sys




if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")
    
    print("Server running")

    """
    Quando uso lo Skeleton per delega, lato business logic devo:
        - istanziare un oggetto RealSubject che implementa il mio servizio (Subject)
        - istanziare uno Skeleton, passando il riferimento a RealSubject che è quello che mi implementa il servizio
        - far partire lo skeleton con l'istanza di Skeleton
    """
    serviceImpl = ServiceImpl()
    skeleton = Skeleton(int(PORT), serviceImpl)
    skeleton.run_skeleton()
