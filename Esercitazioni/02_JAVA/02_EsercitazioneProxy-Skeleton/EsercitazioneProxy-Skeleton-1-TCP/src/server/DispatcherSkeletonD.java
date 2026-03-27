package server;

import java.net.*;
import java.io.*;

import dispatcher.*;

public class DispatcherSkeletonD implements IDispatcher {
	
	
	private IDispatcher dispatcher; 
	private int port;
	
	
	public DispatcherSkeletonD ( IDispatcher d, int p ){
		dispatcher = d;
		port = p;
	}
	
	
	
	public void runSkeleton () {
		
		try{
			ServerSocket server = new ServerSocket ( port );
			
			System.out.println ("[DISPATCHER SKELETON] Waiting for connection (*D*)... ");
			
			while ( true ){
				
				Socket s = server.accept();
				
				ServerThread t = new ServerThread ( s, this );
				t.start();
			}
			
		}catch ( IOException e ){
			e.printStackTrace();
		}
		
	}
	
	
	public void sendCmd ( int cmd ){
		dispatcher.sendCmd(cmd);
	}
	
	public int getCmd(){
		return dispatcher.getCmd();
	}

}
