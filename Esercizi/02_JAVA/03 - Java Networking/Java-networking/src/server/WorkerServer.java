package server;

import java.io.*;
import java.net.*;

public class WorkerServer extends Thread {
	
	private Socket s ; 
	
	public WorkerServer ( Socket skt ){
		s=skt;
	}
	
	public void run (){
		
		try{
			
			/*
			 * creazione degli stream per la comunicazione con la socket lato 
			 * client
			 */
			
			DataInputStream fromClient = new DataInputStream ( s.getInputStream());
			DataOutputStream toClient = new DataOutputStream ( s.getOutputStream());	
		
			// attesa e stampa della string inviata dal client
			System.out.println ("	[Server-Worker]: attesa stringa dal client..." );
			Integer st = fromClient.readInt();

			System.out.println ("	[Server-Worker]: stringa ricevuta < " + st + ">. Invio risposta." );
		
			// invio della stringa di risposta
			toClient.writeUTF("richiesta ricevuta");
		
			fromClient.close();
			toClient.close();
			s.close();
	

			
		}catch (IOException e ){
			e.printStackTrace();
		}
		
	}

}
