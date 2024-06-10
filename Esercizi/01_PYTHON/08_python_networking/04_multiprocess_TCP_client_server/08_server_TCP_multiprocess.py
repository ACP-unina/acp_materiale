import socket
import multiprocess as mp

# process function
def proc_fun(c):


    # data received from client
    data = c.recv(1024)

    # reverse the given string from client
    data = data[::-1]

    # send back reversed string to client
    c.send(data)

    # connection closed
    c.close()


if __name__ == '__main__':

    host = ""
    cur_port = 0

    # create and bind a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, cur_port))
    cur_port = s.getsockname()[1] # get used port

    print("Socket binded to port", cur_port)

    s.listen(5)
    print("Socket is listening")

    while True:

        # establish a connection with client
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])

        # start a new process
        p = mp.Process(target=proc_fun, args=(c,))
        p.start()

    s.close()


