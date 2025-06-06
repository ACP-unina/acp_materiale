package server;

import java.net.*;
import java.io.*;

import dispatcher.*;

public abstract class DispatcherSkeletonE implements IDispatcher {
	
	private int port;
	
	public DispatcherSkeletonE (int port){
		this.port = port;
	}
	
	public void runSkeleton () {
		
		try{
			DatagramSocket socket = new DatagramSocket( port );
			
			System.out.println ("[DISPATCHER SKELETON] Waiting for connection (*E*)... ");
			
			while ( true ){

				byte[] buffer = new byte[65508];
				DatagramPacket request = new DatagramPacket(buffer, buffer.length);
				socket.receive(request);
				
				ServerThread t = new ServerThread ( socket, request, this );
				t.start();
			}
			
		}catch ( IOException e ){
			e.printStackTrace();
		}
		
	}	

}
