import sys
from dispatcherImpl import dispatcherImpl
from dispatcherSkeleton import DispatcherSkeleton

if __name__ == "__main__":

    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("Please, specify HOST and/or PORT args")
        sys.exit(-1)
    
    """
    Quando uso lo Skeleton per ereditarietà, lato business logic devo:
        - istanziare un oggetto RealSubject che estende lo Skeleton
        - far partire lo skeleton con l'istanza di RealSubject che ho appena creato
    """

    print("Dispatcher Server running...")

    dispatcherImpl = dispatcherImpl()
    dispatcherSkeleton = DispatcherSkeleton(HOST, int(PORT), dispatcherImpl)
    dispatcherSkeleton.run_skeleton()

    

