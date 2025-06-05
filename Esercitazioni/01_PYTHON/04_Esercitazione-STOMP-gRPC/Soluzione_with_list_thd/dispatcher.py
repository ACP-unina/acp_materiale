import sys
import time
import grpc
import service_pb2_grpc
import service_pb2
import stomp
from multiprocess import Process


# process function
def proc_fun(port, mess):

    request = mess.split('-')[0]

    # Create connection
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # Connect and subscribe to the queue 'request'
    conn.connect(wait=True)

    # Create the channel
    channel = grpc.insecure_channel('localhost:' + str(port))

    # Obtaining the stub
    stub = service_pb2_grpc.ServiceStub(channel)

    if request == "deposita" :
        id = mess.split('-')[1]
        prod = mess.split('-')[2]
        result = stub.deposita(service_pb2.Item(id=int(id), product=prod))
        print("[DISPATCHER] Response:", result)
        conn.send('/queue/response', result.value)
    
    elif request == "preleva":
        result = stub.preleva(service_pb2.Empty())
        print("[DISPATCHER] Response:", str(result))
        conn.send('/queue/response', str(result.id) + "-" + result.product)

    elif request == "svuota":

        for result in stub.svuota(service_pb2.Empty()):
            print("[DISPATCHER] Response:", str(result))
            conn.send('/queue/response', str(result.id) + "-" + result.product)
    
    


# Listener
class MyListener(stomp.ConnectionListener):
    
    def __init__(self, port):
        self.port = port

    def on_message(self, frame):
        
        print('[DISPATCHER] Request received: "%s"' % frame.body)

        # Start a process to serve the request
        p = Process(target=proc_fun, args=(self.port, frame.body))
        p.start()



if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")

    # Create connection
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # Set the listener
    conn.set_listener('', MyListener(PORT))

    # Connect and subscribe to the queue 'request'
    conn.connect(wait=True)
    conn.subscribe(destination='/queue/request', id=1, ack='auto')
    
    print("[DISPATCHER] Waiting for request ... ")

    # Keep the listener active
    while True:
        time.sleep(60)
   
