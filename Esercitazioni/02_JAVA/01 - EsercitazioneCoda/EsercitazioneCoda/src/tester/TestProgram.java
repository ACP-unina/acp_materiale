package tester;

import coda.*;
import codaimpl.*;

public class TestProgram {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	
		/*
		 * E' possibile variare i meccanismi di sincronizzazione della coda
		 * instanziando un opportuno wrapper (Synchr, Lock, oppure Sem)
		 * 
		 * per es., Coda wrapper = new CodaWrapperSynchr( coda );
		 * 
		 */
		
		
		Coda coda = new CodaCircolare ( 5);				// instanzia una coda circolare SENZA sincronizzazione
		
		Coda wrapper = new CodaWrapperSem( coda );	// creazione del 'wrapper' (decorator) responsabile della
														// sincronizzazione
		
		int nthreads = 100;
		WorkerThread[] workers = new WorkerThread [ nthreads ];
		
		
		for ( int i=0; i<nthreads; i++ ){
			if (	i%2 == 0 )
				workers[i] = new WorkerThread ( wrapper, true );	//crea un thread di inserimento
			else
				workers[i] = new WorkerThread ( wrapper, false );	//crea un thread di prelievo

			workers[i].start();			
		}
		
		
		for ( int i=0; i<nthreads; i++ ){
			try{
				workers[i].join();
			}catch( InterruptedException e ){
				e.printStackTrace();
			}
		}
		
		
	}
}
