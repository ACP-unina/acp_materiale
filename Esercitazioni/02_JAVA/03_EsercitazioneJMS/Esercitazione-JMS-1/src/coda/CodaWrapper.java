package coda;

public abstract class CodaWrapper implements Coda {
	
	protected Coda coda;
	
	public CodaWrapper ( Coda c ){
		coda=c;
	}
	
	/*
	 * segue implementazione metodi empty / full / getSize;
	 * 
	 * NOTA: *non* sono implementati inserisci e preleva -astratti-, al fine di 
	 * 'forzarne' l'implementazione da parte dei concrete decorator (per es. CodaWrapperSynchr);
	 * a tal fine, CodaWrapper e' una classe astratta.
	 * 
	 */
	
	
	public boolean empty(){
		return coda.empty();
	}
	
	public boolean full(){
		return coda.full();
	}
	
	public int getSize(){
		return coda.getSize();
	}

}
