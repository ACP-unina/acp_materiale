from serviceImpl import ServiceImpl
import threading, sys


if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")
        sys.exit(-1)
    
    print("Server running")

    """
    Quando uso lo Skeleton per ereditarietà, lato business logic devo:
        - istanziare un oggetto ServiceImpl che estende lo Skeleton
        - far partire lo skeleton con l'istanza di ServiceImpl che ho appena creato
    """

    serviceImpl = ServiceImpl(int(PORT))
    serviceImpl.run_skeleton()
