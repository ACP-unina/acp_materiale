package server;

import java.net.*;
import java.io.*;

import dispatcher.*;

public abstract class DispatcherSkeletonE implements IDispatcher {
	
	private int port;
	
	public DispatcherSkeletonE ( int p ){
		port=p;
	}
	
	public void runSkeleton () {
		
		try{
			ServerSocket server = new ServerSocket ( port );
			
			System.out.println ("[DISPATCHER SKELETON] Waiting for connection (*E*)... ");
			
			while ( true ){
				Socket s = server.accept();
				
				ServerThread t = new ServerThread ( s, this );
				t.start();
			}
			
		}catch ( IOException e ){
			e.printStackTrace();
		}
		
	}
		

}
