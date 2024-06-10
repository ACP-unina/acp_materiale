import sys, stomp
    

if __name__ == "__main__":

    try:
            MSG = sys.argv[1]
    except IndexError:
            print("Please, specify MSG arg")

    #conn = stomp.Connection([('127.0.0.1', 61613)])
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False) # To use to send TextMessage to a JMS-based application
    conn.connect(wait=True)

    conn.send('/queue/test', MSG)
    
    print("Message: -", MSG, "- sent")

    conn.disconnect()
