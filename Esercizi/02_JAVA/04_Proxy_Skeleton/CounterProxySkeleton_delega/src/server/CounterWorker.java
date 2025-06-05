package server;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

import service.ICounter;

public class CounterWorker extends Thread{
		
		Socket s;
		ICounter count;
		
		public CounterWorker (Socket s, ICounter count){
			
			this.s = s;
			this.count = count;
		}
		
		public void run() {
			
			try {
				
				DataOutputStream ostream = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
			    DataInputStream istream = new DataInputStream(new BufferedInputStream(s.getInputStream()));
		 
			    // lettura dell'operazione
				String operation = istream.readUTF();
			    System.out.println("Servo l'operazione: " + operation);
	    		   
			    //unmarshalling e invocazione sul servizio reale 
			    if (operation.equals("inc")) {
			    	
			    	count.inc();
			    		
			    } else if (operation.equals("sum")) {
			    	
			    	int value = istream.readInt();
			    	count.sum(value);
			    	
			    } else if (operation.equals("sqr")) {
			    
			    	count.square();
			    
			    } else if  (operation.equals("get")) {
			    
			    	ostream.writeInt(count.get());

					/* Flushing a stream ensures that all data that has been written 
						to that stream is output, including clearing any that may have been buffered.
					 */

			    	ostream.flush();
			    	
			    }
	    	
			} catch (IOException e) {
				// Eccezione dovuta alle socket
				e.printStackTrace();
			}
		}
}
