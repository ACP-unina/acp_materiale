from MagazzinoImpl import MagazzinoImpl

if __name__ == "__main__":
    
    IP = "localhost"
    PORT = 0
    QUEUE_SIZE = 5

    magazzino = MagazzinoImpl(IP, PORT, QUEUE_SIZE)
    magazzino.runSkeleton()

    print("[MAGAZZINO SERVER] Started")