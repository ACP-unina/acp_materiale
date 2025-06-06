package server;

public class DispatcherServer {

	private static final int QUEUE_SIZE = 5;
	public static void main(String[] args) {
		
		
		/*
		 * avvio programma server: 	java server.DispatcherServer num_porta [D|E]
		 * per es., 				java server.DispatcherServer 8000
		 */
		
		 System.out.println("[DISPATCHER SERVER] Server started ... ");

		
		if (args[1].compareTo("D") == 0){
		 /*
		 * implementazione per delega
		 */
		
		
		DispatcherImplD dispatcherD = new DispatcherImplD (QUEUE_SIZE);
		DispatcherSkeletonD skeleton = new DispatcherSkeletonD ( dispatcherD, Integer.valueOf(args[0]) );
		skeleton.runSkeleton();
		
		} else if (args[1].compareTo("E") == 0) {
		
		/*
		 * implementazione per ereditarieta'
		 * 
		 * NOTA: in DispatcherImpl, decommentare 
		 * 'public class DispatcherImpl extends DispatcherSkeletonE' ed il costruttore
		 * 
		 */
		
		DispatcherImplE dispatcherE = new DispatcherImplE ( Integer.valueOf(args[0]), QUEUE_SIZE);
		dispatcherE.runSkeleton();
		}
		else
			System.out.println("Error, please use D for delegate server od E for inheritance server");
		
	}

}
