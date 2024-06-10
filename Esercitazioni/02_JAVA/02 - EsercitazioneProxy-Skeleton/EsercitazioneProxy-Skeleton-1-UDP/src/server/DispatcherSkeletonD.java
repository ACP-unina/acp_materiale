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
			DatagramSocket socket = new DatagramSocket( port );
			
			System.out.println ("[DISPATCHER SKELETON] Waiting for connection (*D*)... ");
			
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
	
	
	public void sendCmd ( int cmd ){
		dispatcher.sendCmd(cmd);
	}
	
	public int getCmd(){
		return dispatcher.getCmd();
	}

}
