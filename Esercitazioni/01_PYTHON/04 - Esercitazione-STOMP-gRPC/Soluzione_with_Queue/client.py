import stomp, random, time
    
# Listener
class MyListener(stomp.ConnectionListener):

    def on_message(self, frame):

        # Printing the obtained response
        print('[CLIENT] Received response: "%s"' % frame.body)


if __name__ == "__main__":

    # Create connection
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # Set the listener
    conn.set_listener('', MyListener())

    # Connect and subscribe to the queue 'response'
    conn.connect(wait=True)
    conn.subscribe(destination='/queue/response', id=1, ack='auto')

    # Make the request
    products = ['smartphone', 'laptop']
    for i in range(15):
        
        if (i < 10):
                  
                request = "deposita"
                id = random.randint(1,100)
                product = products[(i%2)]
                MSG = request + "-" + str(id) + "-" + product


        else:
  
            MSG = "preleva"

        # Send the request on the queue 'request'
        conn.send('/queue/request', MSG)

        print("[CLIENT] Request: ", MSG)

    # Make 'svuota' request
    MSG = "svuota"

    # Send the request on the queue 'request'
    conn.send('/queue/request', MSG)

    print("[CLIENT] Request: ", MSG)


    while True:
        time.sleep(60)
    
    conn.disconnect()
