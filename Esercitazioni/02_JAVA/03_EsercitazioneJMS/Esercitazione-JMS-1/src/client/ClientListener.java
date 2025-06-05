package client;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;

public class ClientListener implements MessageListener{

	@Override
	public void onMessage(Message message) {
		
		MapMessage msg = (MapMessage)message;
		
		try {
			System.out.println("[CLIENT-LISTENER] Ricevuto messaggio dalla coda 'Risposta' : " + msg.getInt("valore"));
		} catch (JMSException e) {
			e.printStackTrace();
		}
		
	}
	
}
