package magazzino;

import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;

import coda.Coda;

public class MagazzinoListener implements MessageListener{
	
	private Coda coda;
	private QueueConnection qconn;
	
	public MagazzinoListener(Coda coda, QueueConnection qconn) {
		
		this.coda = coda;
		this.qconn = qconn;
	}

	@Override
	public void onMessage(Message message) {
				
		MapMessage mm = (MapMessage)message;
		
		MagazzinoThread mt = new MagazzinoThread (coda, mm, qconn);
		mt.start();
		
	}

}
