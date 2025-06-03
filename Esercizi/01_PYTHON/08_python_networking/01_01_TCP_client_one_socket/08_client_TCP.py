import socket
import sys
import time  # Import time module for latency measurement

IP = 'localhost'

def client(PORT, s):
    
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!\n"

    start_time = time.time()  # Record the time before sending the request
    s.send(MESSAGE.encode("utf-8"))

    data = s.recv(BUFFER_SIZE)
    end_time = time.time()  # Record the time after receiving the reply

    latency = (end_time - start_time) * 1000  # Convert to milliseconds

    print(f"Received data: {data.decode('utf-8')}")
    print(f"Round-trip latency: {latency:.3f} ms")

    #s.close()

if __name__ == "__main__":
    try:
        PORT = int(sys.argv[1])  # Convert input to integer
    except (IndexError, ValueError):
        print("Please specify a valid PORT as an argument.")
        sys.exit(1)

    ## use only on socket for client requests
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    ## be sure server does not close connection after first send

    while True:
        client(PORT, s)
        time.sleep(1)
