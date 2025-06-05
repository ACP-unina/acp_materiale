package server;

import java.io.*;
import java.net.*;

public class TCPServer {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		try {
			InetAddress host = InetAddress.getByName("localhost"); // specifico un host utilizzando la classe InetAddress
			ServerSocket server = new ServerSocket(8050, 50, host);
			System.out.println ("[Server]: in attesa su porta 8050." );
			
			while ( true ){
				Socket s = server.accept();
				System.out.println ("[Server]: nuovo client, avvio del thread Worker." );
				
				/*
				 * creazione ed avvio del thread worker responsabile della 
				 * gestione della connessione con il client
				 */
				
				WorkerServer w = new WorkerServer (s);
				w.start();			
			}
			
		}catch ( IOException e ){
			e.printStackTrace();
		}
	}
}
