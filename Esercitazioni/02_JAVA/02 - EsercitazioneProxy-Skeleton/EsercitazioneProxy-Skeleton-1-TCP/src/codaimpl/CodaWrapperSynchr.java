package codaimpl;

import coda.*;

public class CodaWrapperSynchr extends CodaWrapper {

	
	public CodaWrapperSynchr( Coda c ){
		super (c);		
	}
	
	
	/*
	 * implementazione delle procedure di accesso alla
	 * coda con blocchi sincronizzati
	 */
	
	public void inserisci( int i){
		
		synchronized ( coda ){
			
			while ( coda.full() ){
				try{
					coda.wait();
				}catch ( InterruptedException e ){
					e.printStackTrace();
				}
			}
			
			coda.inserisci(i);
			
			coda.notifyAll();
		}
	}
	
	
	public int preleva(){
		int x=0;
		
		synchronized ( coda ){
			
			while ( coda.empty() ){
				try{
					coda.wait();
				}catch( InterruptedException  e){
					e.printStackTrace();
				}
			}
			
			x = coda.preleva();
			
			coda.notifyAll();
		}

		return x;
	}
	
}
