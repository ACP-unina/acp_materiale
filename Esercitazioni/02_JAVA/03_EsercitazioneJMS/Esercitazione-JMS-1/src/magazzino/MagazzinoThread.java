package magazzino;

import javax.jms.*;
import coda.*;

public class MagazzinoThread extends Thread {

	private Coda coda; 
	private MapMessage mm ;
	private QueueConnection qconn;
	
	public MagazzinoThread ( Coda c, MapMessage m, QueueConnection qc ){
		coda=c;
		mm=m;
		qconn = qc; 
	}
	
	public void run (){
		try{
			
			String op = mm.getString("operazione");
			int val = mm.getInt("valore");
			
			
			if ( op.compareTo("deposita") == 0 ){
				System.out.println ( "	[MAGAZZINO-THREAD]: operazione = " + mm.getString("operazione") 
						+ " , valore = " + mm.getInt("valore"));
				coda.inserisci( val );
			}else{
				System.out.println ( "	[MAGAZZINO-THREAD]: operazione = " + mm.getString("operazione") );
				val = coda.preleva();
				
				QueueSession qsession = qconn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
				
				/*
				 * Il metodo getJMSReplyTo consente ad un receiver di ottenere
				 * il riferimento ad una Destination (in questo caso la coda 'Risposta'
				 * impostata dal Client) scelta da un sender.
				 * 
				 *  NOTA: Si veda anche setJMSReplyTo() nel Client
				 * 
				 */
				QueueSender qsender = qsession.createSender( (Queue) mm.getJMSReplyTo());
				
				/*
				 * Creazione-invio di un MapMessage che restituisce al Client 
				 * l'id numerico nel caso di una richiesta di tipo preleva. 
				 * Nel MapMessage inserisco anche il Correlation ID fornito tramite il messaggio di richiesta.
				 * Questro permetterà al Client di ricevere solo i messaggi di risposta alla sue richieste.
				 */
				MapMessage reply = qsession.createMapMessage();
				
				reply.setString("operazione", "risultato");
				reply.setInt("valore", val);

				reply.setJMSCorrelationID(mm.getJMSCorrelationID());
				
				qsender.send( reply );
				
				qsender.close();
				qsession.close();
				
			}
		}catch ( JMSException e){
			e.printStackTrace();
		}
	}
	
	
}