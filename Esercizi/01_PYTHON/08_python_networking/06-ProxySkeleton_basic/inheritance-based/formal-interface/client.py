from proxy import Proxy
import sys

if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
        MESSAGE = sys.argv[2]
    except IndexError:
        print("Please, specify PORT and MESSAGE args...")
    
    print("Client: Generating request on port = ", PORT, " with message = ", MESSAGE)
    proxy = Proxy(int(PORT))
    stringa_invertita = proxy.inverti_stringa(MESSAGE)
    print("Client: stringa_invertita => ", stringa_invertita)
    
