import time
import stomp
    

class MyListener(stomp.ConnectionListener):
    
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        print('received a message')
        print('text: "%s"' % frame.body)
        print('headers: "%s"' % frame.headers)
        print('cmd: "%s"' % frame.cmd)

if __name__ == "__main__":
    
    conn = stomp.Connection([('127.0.0.1', 61613)])

    conn.set_listener('', MyListener(conn))

    conn.connect(wait=True)
    conn.subscribe(destination='/queue/test', id="1", ack='auto')
    
    print('Receiver waiting for messages...')

    time.sleep(60)

    conn.disconnect()

