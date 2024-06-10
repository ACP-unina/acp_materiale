import sys, stomp, random
    
 
if __name__ == "__main__":
 
    try:
            MSG = sys.argv[1]
    except IndexError:
            print("Please, specify MSG arg")
 
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)
 
    txid = conn.begin() # Start transaction
 
    try:
        for i in range(3):
        
                print(f'#{i} Message: - {MSG} - sending...')
                # Emulating a problem during the transaction
                value = random.randint(0, 1)
                if value == 0:
                        raise IOError("Problem while sending a message")
                
                conn.send('/topic/mytesttopic', MSG + "-" + str(i), transaction=txid) # Send message in the transaction
                print(f'#{i} Message: - {MSG} - sent!!!')
        
 
    except IOError as e:
        print(e)
        print("Abort transaction")
        conn.abort(txid) # Abort transaction
    else:           
        conn.commit(txid) # Commit transaction
        print("Transaction committed")
    
    conn.disconnect()
 