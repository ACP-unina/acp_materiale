package server;

import coda.CodaWrapper;
import codaimpl.CodaCircolare;
import codaimpl.CodaWrapperLock;

import dispatcher.IDispatcher;


public class DispatcherImpl implements IDispatcher {		// impl. per delega
	
//public class DispatcherImpl extends DispatcherSkeletonE {	// impl. per ereditarieta'

	private CodaWrapper codaWrapper; 
	
	/*
	 * in caso di implementazione per erditarieta', DispatcherImpl inizializza port in DispatcherSkeletonE
	 */
	//public DispatcherImpl  ( int p, int size ){
	//	super (p); 
	//  	CodaCircolare coda = new CodaCircolare(size);
	//  	codaWrapper = new CodaWrapperLock(coda);
	//}
	
	public DispatcherImpl  (int size){
	
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
