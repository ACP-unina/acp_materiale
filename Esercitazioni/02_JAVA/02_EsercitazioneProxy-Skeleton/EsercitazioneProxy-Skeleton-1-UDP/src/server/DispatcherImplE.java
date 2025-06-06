package server;

import coda.CodaWrapper;
import codaimpl.CodaCircolare;
import codaimpl.CodaWrapperLock;

public class DispatcherImplE extends DispatcherSkeletonE {		// impl. per ereditarietà

	private CodaWrapper codaWrapper; 
	
	public DispatcherImplE  (int port, int size){
	
		super(port); 
		CodaCircolare coda = new CodaCircolare(size);
		codaWrapper = new CodaWrapperLock(coda);
	}

	public void sendCmd ( int cmd ){
		System.out.println ("		+ [DISPATCHER IMPL] sendCmd: " + cmd );
		codaWrapper.inserisci(cmd);
	}
	
	public int getCmd(){
		int command = codaWrapper.preleva();
		System.out.println ("		+ [DISPATCHER IMPL] getCmd: " + command );	
		return command;
	}
	

}
