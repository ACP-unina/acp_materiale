package server;

public class Server { 
	
	public static void main(String[] args) {
    		

		/* 
		 * NOTA: Nel caso di Skeleton con delega non possiamo fare il run delle Skeleton tramite
		 * count.runSkeleton() ma deleghiamo alla classe Skeleton a cui passiamo un riferimento
		 * dell'oggetto che implementa il servizio (CounterImpl)
		 */ 

		CounterImpl count = new CounterImpl();

		CounterSkeletonDelega skelDelega = new CounterSkeletonDelega(count);
		
		skelDelega.runSkeleton();
		
	}
	
}