package dispatcher;

import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;

import javax.jms.TextMessage;

public class DispatcherMsgListener implements MessageListener {
	
	private QueueConnection qconnection;
	private int port;
	
	public DispatcherMsgListener(QueueConnection qc, int port){

		this.qconnection = qc;
		this.port = port;
	}

	
    @Override
	public void onMessage(Message arg0) {
		
		TextMessage msg = (TextMessage)arg0;
		
		DispatcherThread dt = new DispatcherThread (port, qconnection, msg);
		dt.start();
		
				
	}

}
