package pubsubapp_asynch;

import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.Session;
import javax.jms.Topic;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicSession;
import javax.jms.TopicSubscriber;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class Subscriber {

	public static void main(String[] args) throws NamingException, JMSException {
		
		Hashtable<String, String> properties = new Hashtable<String, String>();
		properties.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
		properties.put("java.naming.provider.url","tcp://127.0.0.1:61616");	
		properties.put("topic.soccer" , "soccernews"); //consumes from the topic soccernews 
		Context jndiContext = new InitialContext(properties);

		TopicConnectionFactory tcf = (TopicConnectionFactory)jndiContext.lookup("TopicConnectionFactory");
		Topic soccer = (Topic)jndiContext.lookup("soccer");

		TopicConnection tc = tcf.createTopicConnection();
		
		//tc.setClientID("MakeItLastConn_1"); //to be used in case of Durable subscription 

		TopicSession ts = tc.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
		//TopicSubscriber subscriber = ts.createSubscriber(soccer);
		//TopicSubscriber subscriber = ts.createDurableSubscriber(soccer, "MakeItLastConn_1");
		TopicSubscriber subscriber = ts.createSubscriber(soccer, "propInt=10", false);
		
		// creo un message listener per attivare la ricezione asincrona	
		MyListener msgl = new MyListener();
		subscriber.setMessageListener(msgl);

		tc.start();  // tells the messaging provider to start message delivery
		
		System.out.println("Listener set...");
		
		/*subscriber.close(); // When these three lines are commented, the subscriber keeps on listening
		ts.close();
		tc.close();*/
		
			}

}
