package server;

import dispatcher.*;

import java.io.*;
import java.net.*;
import java.util.StringTokenizer;

public class ServerThread extends Thread {

	private DatagramSocket s; 
	private DatagramPacket request;
	private IDispatcher dispatcher;
	
	private static final String separator = "#";
	
	public ServerThread ( DatagramSocket sk, DatagramPacket req, IDispatcher d ){
		s=sk;
		request = req;
		dispatcher = d; 
	}
	
	
	public void run ( ){
		
		System.out.println ("	[DISPATCHER THREAD] run thread! " );
		
		try{
			
			
			String message = new String(request.getData(), 0, request.getLength());

			StringTokenizer tokenizer = new StringTokenizer(message, separator);
			
			String method = tokenizer.nextToken();
			int x;
			
			if ( method.compareTo("sendCmd") == 0 ){
				
				x = Integer.valueOf(tokenizer.nextToken());
				System.out.println ("	[DISPATCHER THREAD] method: " + method + ", " + x);
				
				dispatcher.sendCmd (  x);

				String reply = new String("ack");
				
				DatagramPacket response = new DatagramPacket(reply.getBytes(), reply.getBytes().length, request.getAddress(), request.getPort());
				
				s.send(response);
				
			}
			else if ( method.compareTo("getCmd") == 0 ){
				
			
				System.out.println ("	[DISPATCHER THREAD] method: " + method);
				x= dispatcher.getCmd(); 
				
				String reply = Integer.toString(x);
				
				DatagramPacket response = new DatagramPacket(reply.getBytes(), reply.getBytes().length, request.getAddress(), request.getPort());
				
				s.send(response);
				
			}else {
				System.out.println ("[DISPATCHER THREAD] Error: unknown method!");
				String reply = new String("failed");
				
				DatagramPacket response = new DatagramPacket(reply.getBytes(), reply.getBytes().length, request.getAddress(), request.getPort());
				
				s.send(response);
			}
			
			System.out.println ();
			
			
		}catch ( IOException e ){
			e.printStackTrace();
		}
		
	}
	
	
}
