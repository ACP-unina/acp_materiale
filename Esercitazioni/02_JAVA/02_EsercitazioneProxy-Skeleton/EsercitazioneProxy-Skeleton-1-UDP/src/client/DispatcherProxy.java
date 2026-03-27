package client;

import java.net.*;
import java.io.*;

import dispatcher.*;

public class DispatcherProxy implements IDispatcher {
	
	private String addr;
	private int port;
	private DatagramSocket socket;
	
	
	public DispatcherProxy ( String a, int p ){
		addr = new String ( a);
		port = p;	

		try {
			socket = new DatagramSocket();
		} catch (SocketException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	
	public void sendCmd ( int cmd ){

		String message = new String ("sendCmd#" + cmd + "#");
		
		try{
			DatagramPacket request = new DatagramPacket(message.getBytes(), message.getBytes().length, InetAddress.getByName(addr), port);

			System.out.println("[DISPATCHER PROXY] Sending sendCmd with command: " + cmd);

			socket.send(request);
			
			byte[] buffer = new byte[65508];
			DatagramPacket reply = new DatagramPacket(buffer, buffer.length);

			socket.receive(reply);

			String response = new String(reply.getData(), 0, reply.getLength());

			System.out.println("[DISPATCHER PROXY] Received response: " + response);
			
			
		}catch (UnknownHostException u ){
			u.printStackTrace();
		}catch (IOException e ){
			e.printStackTrace();
		}
		
	}
	
	
	public int getCmd(){
		
		int x=0;

		String message = new String ("getCmd#");
		
		try{
			
			DatagramPacket request = new DatagramPacket(message.getBytes(), message.getBytes().length, InetAddress.getByName(addr), port);

			System.out.println("[DISPATCHER PROXY] Sending getCmd");
			socket.send(request);

			byte[] buffer = new byte[65508];
			DatagramPacket reply = new DatagramPacket(buffer, buffer.length);

			socket.receive(reply);

			String response = new String(reply.getData(), 0, reply.getLength());
			x = Integer.valueOf(response);

			System.out.println("[DISPATCHER PROXY] Received: " + x);
			
		}catch (UnknownHostException u ){
			u.printStackTrace();
		}catch (IOException e ){
			e.printStackTrace();
		}
		
		return x;
	}
	

}
