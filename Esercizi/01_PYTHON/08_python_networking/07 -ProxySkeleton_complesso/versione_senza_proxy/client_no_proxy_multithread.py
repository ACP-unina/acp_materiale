
import random, time, sys, socket

import threading as mt
    

BUFFER_SIZE=1024
N_CLIENTS = 5
N_reqs_per_client = 3

def generate_client_reqs():
    
        for i in range(N_reqs_per_client):
    
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
            s.connect((HOST, int(PORT)))

            value_to_deposit = random.randint(0,3) #tra 0-leggi, 1-scrivi, 2-configura, 3-reset. Ciascun thread effettua 3 richieste.

            request = "sendCmd"
            message_to_send = request + "-" + str(value_to_deposit)        
            
            thread_name = mt.current_thread().name
            print(f'[CLIENT Thread name: {thread_name}] using socket ref: {hex(id(s))}')
            print(f'[CLIENT Thread name: {thread_name}] \t\t\tSending # {i} message: {message_to_send}\n')
            
            time.sleep(random.randint(2,4))
            s.send(message_to_send.encode("utf-8"))

            ## receive response to deposita
            print(f'[CLIENT Thread name: {thread_name}] \t\t\twaiting for result for #{i} request...\n')
            
            data = s.recv(BUFFER_SIZE).decode('utf-8')
            print(f'[CLIENT Thread name: {thread_name}] \t\t\tdata received: {data:s} for #{i} request\n')

            s.close()
        

if __name__ == "__main__":

    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("Please, specify PORT and MESSAGE args...")
        sys.exit(-1)

        
    # Make the requests
    clients = []
    for i in range (N_CLIENTS):

        # creazione del process con callable object (func)
        cli = mt.Thread(target=generate_client_reqs)

        cli.start()

        clients.append(cli)    

    
    # waiting consumers termination
    for i in range (N_CLIENTS):

        clients[i].join()
        
        

