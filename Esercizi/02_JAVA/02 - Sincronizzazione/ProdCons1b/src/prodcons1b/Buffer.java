package prodcons1b;

public class Buffer {
	
	private long content;
	private boolean full;
	
	
	public Buffer (){
		content = 0;
		
		/*
		 * condizione iniziale: false.
		 * FALSE = contenuto buffer non prodotto
		 * TRUE  = contenuto buffer prodotto
		 */
		
		full = false; 	
	}
	
	
	public synchronized void produci (){
		
		System.out.println ( Thread.currentThread().getName() + ":  invocazione produci" );

		while ( full ){ 	//TODO condizione produci
			System.out.println ( Thread.currentThread().getName() + ":  in attesa (buffer pieno)" );

			try{
				wait ();
			}catch ( InterruptedException e ){
				e.printStackTrace();
			}	
		}
	
		content = System.currentTimeMillis();
		System.out.println ( Thread.currentThread().getName() + ":  prodotto = " + content );

		full = true ; //TODO aggiorna condizione
		
		notifyAll ();
		
	}
	
	
	public synchronized void consuma  () {
		
		System.out.println ( Thread.currentThread().getName() + ":  invocazione consuma" );
		
		while ( !full ){ 	//TODO condizione consuma
			System.out.println ( Thread.currentThread().getName() + ":  in attesa (buffer vuoto)" );

			try{
				wait ();
			}catch ( InterruptedException e ){
				e.printStackTrace();
			}	
		}
	
		System.out.println ( Thread.currentThread().getName() + ":  consumato = " + content );

		full = false ; //TODO aggiorna condizione
		
		notifyAll ();
		
		
			
	}

}