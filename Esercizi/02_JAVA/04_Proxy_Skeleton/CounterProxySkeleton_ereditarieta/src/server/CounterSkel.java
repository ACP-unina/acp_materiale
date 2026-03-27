package server;
import service.*;


import java.net.*;
import java.io.*;

public abstract class CounterSkel implements ICounter {

	
	public void runSkeleton() {
		
		ServerSocket serverSocket = null;
		Socket socket = null;
		
		try {
			
			serverSocket = new ServerSocket(2500); //socket server
			System.out.println("Server in ascolto sulla porta 2500");
			
			while (true){
				
				socket = serverSocket.accept();
				CounterWorker st = new CounterWorker(socket, this);
				st.start();
			}
			
		} catch (IOException e) {
			// Eccezione dovuta alle socket
			e.printStackTrace();
		}
	}

}
		