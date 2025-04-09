import socket
import sys
import time  # Import time module for latency measurement

def client(port):
    msgClient = "Ciao server!"
    serverAddressPort = ("localhost", port)
    bufferSize = 1024

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    print("[Client]: Invio dati al server. msg:", msgClient)

    start_time = time.time()  # Record time before sending request
    s.sendto(msgClient.encode("utf-8"), serverAddressPort)

    msgServer, addr = s.recvfrom(bufferSize)
    end_time = time.time()  # Record time after receiving reply

    latency = (end_time - start_time) * 1000  # Convert to milliseconds

    print("[Client]: Risposta server:", msgServer.decode("utf-8"))
    print(f"[Client]: Round-trip latency: {latency:.3f} ms")

    s.close()

if __name__ == "__main__":
    try:
        port = int(sys.argv[1])  # Convert input to integer
    except (IndexError, ValueError):
        print("Please specify a valid PORT as an argument.")
        sys.exit(1)

    client(port)
