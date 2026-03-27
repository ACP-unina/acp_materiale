package tester;

import coda.*;

public class WorkerThread extends Thread {

	
	private Coda wrapper;			 
	private boolean flag;			//se true, invoca il metodo di inserimento 
	
	public WorkerThread ( Coda w, boolean f ){
		wrapper=w;
		flag = f;
	}
	
	public void run (){
		
		if ( flag )
			wrapper.inserisci(	1+(int)(Math.random()* 100)	);		//int random in [1;100]
		else
			wrapper.preleva();
		
	}
	
}
