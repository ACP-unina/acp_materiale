package client;
import service.ICounter;
import java.io.*;
import java.net.*;

public class CounterProxy implements ICounter {

	private String host;
	private int port;
	
	// costruttore, richiede in ingresso l'indirizzo del server
	public CounterProxy(String host, int port) {
		
		this.host = host;
		this.port = port;
	}
	
	// metodo per l'invocazione remota del servizio getValue
	public int get() {
		
		try {
		
			Socket soc = new Socket (host, port);
			DataOutputStream ostream= new DataOutputStream (new BufferedOutputStream(soc.getOutputStream()));
			DataInputStream istream = new DataInputStream(new BufferedInputStream(soc.getInputStream()));
			
			// marshalling
			ostream.writeUTF("get");
			ostream.flush();
			
			int x = istream.readInt();
			
			soc.close();
			
			return x;
			
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return 0;
	}

	// metodo per l'invocazione remota del servizio increment
	public void inc() {
		try {
			
			Socket soc = new Socket (host, port);
			DataOutputStream ostream= new DataOutputStream (new BufferedOutputStream(soc.getOutputStream()));
			
			// marshalling
			ostream.writeUTF("inc");
			ostream.flush();
			
			soc.close();
			
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	
	public void square() {
		try {
			
			Socket soc = new Socket (host, port);
			DataOutputStream ostream= new DataOutputStream (new BufferedOutputStream(soc.getOutputStream()));
			
			// marshalling
			ostream.writeUTF("sqr");
			ostream.flush();
			
			soc.close();
			
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	
	
	// metodo per l'invocazione remota del servizio setValue
	public void sum(int value) {
		try {
			
			Socket soc = new Socket (host, port);
			DataOutputStream ostream= new DataOutputStream (new BufferedOutputStream(soc.getOutputStream()));
			
			// marshalling
			ostream.writeUTF("sum");
			ostream.writeInt(value);
			ostream.flush();
			
			soc.close();
			
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}