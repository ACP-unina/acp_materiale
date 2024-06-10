package server;

public class Server { 
	
	public static void main(String[] args) {
    		
		CounterImpl count = new CounterImpl();

		//CASO 1: avvio dell'oggetto remoto per ereditarieta'
		count.runSkeleton();
	
		//CASO 2: avvio dell'oggetto remoto per delega
		//CounterSkeletonDelega skelDelega = new CounterSkeletonDelega( count );
		//skelDelega.runSkeleton();
		
	}
	
}