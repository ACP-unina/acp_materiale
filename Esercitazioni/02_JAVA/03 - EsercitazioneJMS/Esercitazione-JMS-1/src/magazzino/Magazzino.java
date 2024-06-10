package magazzino;

import javax.jms.*;
import javax.naming.*;

import java.util.Hashtable;

import coda.*;
import codaimpl.*;

public class Magazzino {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Hashtable <String, String> p = new Hashtable <String, String>();
		
		p.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
		p.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
		
		p.put("queue.Richiesta", "Richiesta");
		
		try{
			Context ctx = new InitialContext ( p );
		
			QueueConnectionFactory qconnf = (QueueConnectionFactory)ctx.lookup("QueueConnectionFactory");
			
			/*
			 * Magazzino attende sulla coda 'Richiesta'; MagazzinoThread
			 * invia i messagi di risposta sulla coda 'Risposta'
			 */
			
			Queue queueRequest = (Queue)ctx.lookup("Richiesta");
			
			QueueConnection qconn = qconnf.createQueueConnection();
			qconn.start();
			
			QueueSession qsession = qconn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
			QueueReceiver qreceiver = qsession.createReceiver(queueRequest);
			
			
			/*
			 * Creazione della coda a gestione circolare per la memorizzazione
			 * degli id articolo (Coda presa dall'esercitazione su CodaCircolare)
			 */
			Coda coda = new CodaWrapperSynchr ( new CodaCircolare (10) ) ; 
			
			
			/*
			 * Receive asincrona: il costruttore di MagazzinoListener
			 * riceve coda e qconn 
			 * 
			 */
			
			 /*
				 * Attenzione, la sessione la devo creare dentro il Thread perchè la session 
				 * è sempre single-threaded. Se creassi la sessione fuori il thread potrei
				 * avere problemi di concorrenza. Per questo motivo passo la QueueConnection al Listener
 				*/

			MagazzinoListener l = new MagazzinoListener ( coda, qconn );
			qreceiver.setMessageListener( l );
			
			System.out.println("[MAGAZZINO] Server avviato");
			
			
		}catch ( NamingException e ){
			e.printStackTrace();
		}catch ( JMSException e ){
			e.printStackTrace();
		}

	}

}