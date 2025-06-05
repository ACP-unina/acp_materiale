package pubsubapp_asynch;

import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;

class MyListener implements MessageListener{

	@Override
	public void onMessage(Message arg0) {
		TextMessage mymsg = (TextMessage)arg0;
		System.out.println("Receiving messages ...");
		try {
			String msg = mymsg.getText();
			System.out.println("I am a subscriber. I read the following message ->" + msg);
			System.out.println("The int property of the message is: " + mymsg.getIntProperty("propInt"));
		} catch (JMSException e) {
			e.printStackTrace();
		}
		
	}
	
}
