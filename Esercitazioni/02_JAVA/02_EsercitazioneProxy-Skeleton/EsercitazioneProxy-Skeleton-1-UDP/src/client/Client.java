package client;

public class Client {

	private static final int NUM_THREADS = 5;

	public static void main(String[] args) {
		
		/*
		 * uso: 		java client.Client IP porta
		 * per es.:		java client.Client 127.0.0.1 8000
		 */
		
		String ip_address = args[0];
		int port = Integer.valueOf(args[1]);

		ClientThread threads[] = new ClientThread[NUM_THREADS];

		System.out.println("[CLIENT] Avvio i client thread");

		for (int i = 0; i < NUM_THREADS; i++){
 
			threads[i] = new ClientThread(ip_address, port);
			threads[i].start();
 
 
		}
 
		System.out.println("[CLIENT] Waiting for thread termination");
		
		for (int i = 0; i < NUM_THREADS; i++)

			try {
				threads[i].join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

	}

}
