package client;

import java.util.Hashtable;
import java.util.Random;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueReceiver;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;


public class Client {
	
	private static final int N = 10;
	
	public static void main(String[] args) throws NamingException, JMSException {
		
		Hashtable <String, String> p = new Hashtable <String, String>();
		
		p.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
		p.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
		
		p.put("queue.Richiesta", "Richiesta");
		p.put("queue.Risposta", "Risposta");
		
		Context ctx = new InitialContext ( p );
		
		QueueConnectionFactory qconnf = (QueueConnectionFactory)ctx.lookup("QueueConnectionFactory");
		
		Queue queueRequest = (Queue) ctx.lookup("Richiesta");
		Queue queueResponse = (Queue) ctx.lookup("Risposta");
		
		QueueConnection qconn = qconnf.createQueueConnection();
		qconn.start();
		
		QueueSession qsession = qconn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
		
		// Setup del receiver per la coda di messaggi Risposta
		QueueReceiver qr = qsession.createReceiver(queueResponse);
		ClientListener listener = new ClientListener();
		qr.setMessageListener(listener);
		
		// Setup del sender per la coda di messaggi Richiesta
		QueueSender sender = qsession.createSender(queueRequest);

		// Uso MapMessage come tipo di messaggio perchè ho messaggi
		// del tipo key-value (operazione: tipo_operazione) e (id_articolo: valore)
		MapMessage message = qsession.createMapMessage();
		
		// Generazione random e ciclica delle richieste
		for(int i = 0; i < N; i++){
			
			if( i % 2 == 0 ){
				
				//CASO DEPOSITA
				message.setString("operazione", "deposita");
				Random r = new Random();
				int randomValue = r.nextInt(100);
				message.setInt("valore", randomValue);
				
				sender.send(message);
				System.out.println("[CLIENT] Mandato messaggio deposita con valore: " + randomValue);
			}
			else{
				//CASO PRELEVA
				message.setString("operazione", "preleva");
				
				message.setJMSReplyTo(queueResponse);
				
				sender.send(message);
				System.out.println("[CLIENT] Mandato messaggio preleva");
			}
		}
		
	}
	
}
