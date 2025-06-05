package codaimpl;

import java.util.concurrent.*;
import coda.*;

public class CodaWrapperSem extends CodaWrapper {

	
	private Semaphore postiDisp;
	private Semaphore elemDisp;
	
	
	public CodaWrapperSem ( Coda c ){
		super (c);
		
		postiDisp = new Semaphore ( coda.getSize() );
		elemDisp  = new Semaphore ( 0 ) ;
	}
	
	
	public void inserisci( int i){
		
		try{	
			postiDisp.acquire();
		
			try{
				synchronized ( coda ){
					coda.inserisci(i);
				}	
			}finally {
				elemDisp.release();
			}
		}catch ( InterruptedException e ){
			e.printStackTrace();
		}
		
	}
	
	
	public int preleva(){
		
		int x=0;
		
		try{
			elemDisp.acquire();
			
			try{
				synchronized ( coda ){
					x = coda.preleva();
				}
			}finally{
				postiDisp.release();
			}
		}catch ( InterruptedException e ){
			e.printStackTrace();
		}
		
		return x;
	}
	
	
}