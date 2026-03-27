package codaimpl;

import coda.*;


/*
 * implementazione della coda circolare --> lock free
 */

public class CodaCircolare implements Coda {
	
	
	private int data[];	//gli elementi sono memorizzati in un array gestito in maniera circolare
	
	private int size;
	private int elem;

	
	private int tail;
	private int head;
	
	

	public CodaCircolare( int s){
		size=s;
		elem=0;
		data = new int[size];
		tail=head=0;
	}
	
	// metodi di utilita'

	public boolean full(){
		if ( elem == size )
			return true;
		return false;
	}
	
	public boolean empty(){
		if( elem == 0)
			return true;
		return false;
	}
	
	public int getSize(){
		return size;
	}
	

	//inserisce un elemento 
	
	public void inserisci( int i ){
		data[ tail%size ] =i;
		
		
		try{
			Thread.sleep(101 + (int)(Math.random()*100)  ); //sleep di durata random max pari a 200ms
		}catch ( InterruptedException e ){
			e.printStackTrace();
		}
		
		elem=elem+1;
		System.out.println ("inserito " + i + " (tot = " + elem + " )");
		tail=tail+1;
	}
	
	
	//estrae un elemento 
	public int preleva (){
		int x = data[ head%size ];
		
		
		try{
			Thread.sleep(101 + (int)(Math.random()*400)  ); //sleep di durata random max pari a 500ms
		}catch ( InterruptedException e ){
			e.printStackTrace();
		}
		
		
		elem=elem-1;
		System.out.println ("				prelevato " + x + " (tot = " + elem + " )");
		
		head=head+1;
		return x;
	}
	
	

}