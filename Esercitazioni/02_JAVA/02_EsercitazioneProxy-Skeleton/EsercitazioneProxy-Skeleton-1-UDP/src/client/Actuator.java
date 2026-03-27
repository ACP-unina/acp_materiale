package client;

import dispatcher.*;

import java.io.*;

public class Actuator {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		
		/*
		 * uso: 		java client.Actuator IP porta
		 * per es.:		java client.Actuator 127.0.0.1 8000
		 */

		System.out.println("[Actuator] Started...");
		
		IDispatcher dispatcher = new DispatcherProxy ( args[0], Integer.valueOf( args[1]) );
		int cmd=0;
		
		try{
			FileOutputStream fileOut = new FileOutputStream ( "./cmdlog.txt");
			PrintStream outStream = new PrintStream ( fileOut );
			
			while ( true ){
				
				cmd = dispatcher.getCmd();
				System.out.println ("[ACTUATOR] Received command: " + cmd );
				outStream.println ( "command = "+ cmd);
				
				Thread.sleep( 1000 );	
			} 
				
		}catch ( IOException e ){
			e.printStackTrace();
		}catch ( InterruptedException i ){
			i.printStackTrace();
		}
		
	
	}

}
