
import random, time, sys, socket
    

BUFFER_SIZE=1024

if __name__ == "__main__":

    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("Please, specify PORT and MESSAGE args...")
        sys.exit(-1)

        
    # Make the request
    for i in range(10):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        s.connect((HOST, int(PORT)))

        value_to_deposit = random.randint(0,3) #tra 0-leggi, 1-scrivi, 2-configura, 3-reset. Ciascun thread effettua 3 richieste.

        request = "sendCmd"
        message_to_send = request + "-" + str(value_to_deposit)        
        
        print("[CLIENT] sending message: ", message_to_send)
        time.sleep(2)
        s.send(message_to_send.encode("utf-8"))

        ## receive response to deposita
        print("[CLIENT] waiting for result...")
        data = s.recv(BUFFER_SIZE)

        print("[Client] data received: " + data.decode('utf-8'))

