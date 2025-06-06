package server;

import coda.CodaWrapper;
import codaimpl.CodaCircolare;
import codaimpl.CodaWrapperLock;

import dispatcher.IDispatcher;


public class DispatcherImplD implements IDispatcher {		// impl. per delega

	private CodaWrapper codaWrapper; 
	
	public DispatcherImplD  (int size){
	
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
