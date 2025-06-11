package dispatcher;

import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;

import javax.jms.TextMessage;

public class DispatcherMsgListener implements MessageListener {
	
	private QueueConnection qconnection;
	private MagazzinoGrpc.MagazzinoBlockingStub blockingStub;
	
	public DispatcherMsgListener(QueueConnection qc, MagazzinoGrpc.MagazzinoBlockingStub blockingStub){

		this.qconnection = qc;
		this.blockingStub = blockingStub;
	}

	
    @Override
	public void onMessage(Message arg0) {
		
		TextMessage msg = (TextMessage)arg0;
		
		// ogni qual volta ricevuto un messaggio di richiesta JMS schedulo un thread per la gestione
		DispatcherThread dt = new DispatcherThread (blockingStub, qconnection, msg);
		dt.start();
		
				
	}

}
