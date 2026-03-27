package server;

import dispatcher.*;

import java.io.*;
import java.net.*;

public class ServerThread extends Thread {

	private Socket s; 
	private IDispatcher dispatcher; 
	
	public ServerThread ( Socket sk, IDispatcher d ){
		s=sk;
		dispatcher = d; 
	}
	
	
	public void run ( ){
		
		System.out.println ("	[DISPATCHER THREAD] run thread! " );
		
		try{
			
			
			DataInputStream dataIn = new DataInputStream ( new BufferedInputStream(s.getInputStream()) );
			DataOutputStream dataOut = new DataOutputStream ( new BufferedOutputStream(s.getOutputStream()) );
			
			String method = dataIn.readUTF();
			int x;
			
			if ( method.compareTo("sendCmd") == 0 ){
				
				x=dataIn.readInt();
				System.out.println ("	[DISPATCHER THREAD] method: " + method + ", " + x);
				
				dispatcher.sendCmd (  x);
				
				dataOut.writeUTF("ack");
				
			}
			else if ( method.compareTo("getCmd") == 0 ){
				
			
				System.out.println ("	[DISPATCHER THREAD] method: " + method);
				x= dispatcher.getCmd(); 
				
				dataOut.writeInt ( x);
				
			}else {
				System.out.println ("[DISPATCHER THREAD] Error: unknown method!");
				dataOut.writeUTF("failed");
			}
			
			dataOut.flush();
			
			System.out.println ();
			s.close();
			
			
		}catch ( IOException e ){
			e.printStackTrace();
		}
		
	}
	
	
}
