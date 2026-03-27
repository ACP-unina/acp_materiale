package client;

import java.net.*;
import java.io.*;

import dispatcher.*;

public class DispatcherProxy implements IDispatcher {
	
	private String addr;
	private int port;
	
	
	public DispatcherProxy ( String a, int p ){
		addr = new String ( a);
		port = p;	
	}
	
	
	public void sendCmd ( int cmd ){
		
		try{
			Socket s = new Socket ( addr, port );
			
			DataOutputStream dataOut = new DataOutputStream ( new BufferedOutputStream(s.getOutputStream() ));
			DataInputStream dataIn = new DataInputStream ( new BufferedInputStream(s.getInputStream()) );

			System.out.println("[DISPATCHER PROXY] Sending sendCmd with command: " + cmd);
			
			dataOut.writeUTF("sendCmd");
			dataOut.writeInt ( cmd );
			dataOut.flush();
			
			String response = dataIn.readUTF();	

			System.out.println("[DISPATCHER PROXY] Received response: " + response);
			
			dataIn.close();
			dataOut.close();
			s.close();
			
		}catch (UnknownHostException u ){
			u.printStackTrace();
		}catch (IOException e ){
			e.printStackTrace();
		}
		
	}
	
	
	public int getCmd(){
		
		int x=0;
		
		try{
			
			Socket s = new Socket ( addr, port );
			DataOutputStream dataOut = new DataOutputStream ( s.getOutputStream() );
			DataInputStream dataIn = new DataInputStream ( s.getInputStream() );

			System.out.println("[DISPATCHER PROXY] Sending getCmd");
			dataOut.writeUTF("getCmd");

			x=dataIn.readInt ();

			System.out.println("[DISPATCHER PROXY] Received: " + x);
			
			dataOut.close();
			dataIn.close();
			s.close();
			
		}catch (UnknownHostException u ){
			u.printStackTrace();
		}catch (IOException e ){
			e.printStackTrace();
		}
		
		return x;
	}
	

}
