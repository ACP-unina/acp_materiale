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
    for i in range(1000):
        
        if ( (i%2) == 0):
                  
                request = "deposita"
                id = random.randint(1,100)
                MSG = request + "-" + str(id)


        else:
              
              MSG = "preleva"

        # Send the request on the queue 'request'
        conn.send('/queue/request', MSG)

        print("[CLIENT] Request: ", MSG)

    while True:
        time.sleep(60)
    
    conn.disconnect()
