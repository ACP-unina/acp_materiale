package server;

import java.net.*;
import java.io.*;

import dispatcher.*;

public class DispatcherSkeletonD implements IDispatcher {	

	private IDispatcher dispatcher;  //ricordare di soddisfare il basso accoppiamento!
	// Dependency inversion principle (DIP) o principio di inversione delle dipendenze:
	// Una classe dovrebbe dipendere dalle astrazioni, non da classi concrete.

	private int port;
	
	public DispatcherSkeletonD ( IDispatcher dispatcher, int port ){
		this.dispatcher = dispatcher;
		this.port = port;
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
	
	//delega
	public void sendCmd ( int cmd ){
		dispatcher.sendCmd(cmd);
	}
	
	public int getCmd(){
		return dispatcher.getCmd();
	}

}
