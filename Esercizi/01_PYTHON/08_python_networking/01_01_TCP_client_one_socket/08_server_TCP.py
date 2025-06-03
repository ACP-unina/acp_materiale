import socket

IP = '0.0.0.0'
PORT = 0
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)

cur_port = s.getsockname()[1]

print("server on: ", IP, "port: ", cur_port)

while True:
    conn, addr = s.accept()
    print("client addr: " + str(addr))
    print  ('Connection address: {}' .format(addr))
    toClient= "The world never says hello back!\n"

    """
    ## without a loop the recv is only one message and the connection is closed
    ## with a BrokenPipeError: [Errno 32] Broken pipe client-side

    data = conn.recv(BUFFER_SIZE)
    print ("received data: " + data.decode("utf-8"))

    conn.send(toClient.encode("utf-8"))

    conn.close()
    """

    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print("No DATA, client close connection")
                break  # Client closed connection
            print("received data: " + data.decode("utf-8"))
            conn.send(toClient.encode("utf-8"))
    except ConnectionResetError:
        print("Client disconnected abruptly.")
    finally:
        conn.close()

s.close()
