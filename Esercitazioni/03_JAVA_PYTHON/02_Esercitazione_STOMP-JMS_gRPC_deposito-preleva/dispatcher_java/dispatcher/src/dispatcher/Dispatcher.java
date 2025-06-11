package dispatcher;

import java.util.Hashtable;
import java.util.concurrent.TimeUnit;

import javax.jms.*;
import javax.naming.*;

import io.grpc.Grpc;
import io.grpc.InsecureChannelCredentials;
import io.grpc.ManagedChannel;

public class Dispatcher {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		/*
		 * Il dispatcher crea una destination di coda richieste per parlare con un client Python
		 * Una volta ricevuta la richiesta (asincrona tramite MessageListener) di operazione parlerà tramite Proxy-Skeleton (socket)
		 * verso il server
		 */

		if (args.length != 1) {
			System.out.println("Specificare il numero di porto per la comunicazione lato server!");
			System.exit(-1);
		}

		Hashtable<String, String> properties = new Hashtable<String,String>();
		properties.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
		properties.put("java.naming.provider.url","tcp://127.0.0.1:61616");
		
		properties.put("queue.request", "request");
		properties.put("queue.response", "response");
		
		try {
			
			Context jndiContext = new InitialContext(properties);
			QueueConnectionFactory qcf = (QueueConnectionFactory) jndiContext.lookup("QueueConnectionFactory");
			
			// creo la coda di richieste
			Queue qrequest = (Queue)jndiContext.lookup("request");
			QueueConnection qc = qcf.createQueueConnection();
			qc.start();
			
			QueueSession qs = qc.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
			QueueReceiver receiver = qs.createReceiver(qrequest);
			
			// passo al listener la sessione, la coda di risposte ed il numero di porto (ricevuto da terminale) in modo da inviare il messaggio al server
			int port = Integer.valueOf(args[0]);		

			String target =  "localhost:"+port;

			/// JAVA GRPC client-siede
			/// Creo il managed channel, creo lo stub e invoco il metodo non appena ricevo il messaggio
			ManagedChannel channel = Grpc.newChannelBuilder(target, InsecureChannelCredentials.create()).build();

			MagazzinoGrpc.MagazzinoBlockingStub blockingStub = MagazzinoGrpc.newBlockingStub(channel);
			
			DispatcherMsgListener listener = new DispatcherMsgListener(qc, blockingStub);

			receiver.setMessageListener(listener);
			
			System.out.println("Dispatcher avviato - comunicazione lato server su porto: " + port);

			/*try {
				channel.shutdownNow().awaitTermination(60, TimeUnit.SECONDS);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}*/


		} catch (NamingException e) {
			e.printStackTrace();
		} catch (JMSException e) {
			e.printStackTrace();
		}		
	}

}
