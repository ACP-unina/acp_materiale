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
		
		DispatcherThread dt = new DispatcherThread (blockingStub, qconnection, msg);
		dt.start();
		
				
	}

}
