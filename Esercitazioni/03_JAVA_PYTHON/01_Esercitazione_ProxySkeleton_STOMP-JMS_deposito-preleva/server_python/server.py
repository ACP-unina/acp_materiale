from serviceImpl import ServiceImpl
import socket, sys
import multiprocess as mp

if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")
        sys.exit(-1)
    
    print("Server running on port " + str(PORT))

    # Create the Qeueue
    q = mp.Queue(5)

    # Create the Service and run the Skeleton
    serviceImpl = ServiceImpl(int(PORT), q)
    serviceImpl.run_skeleton()
