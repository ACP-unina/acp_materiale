package dispatcher;

import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.jms.TextMessage;

public class DispatcherThread extends Thread{

    private int port;
    private QueueConnection qconnection;
    private TextMessage msg;
  
    public DispatcherThread(int port, QueueConnection qconnection, TextMessage msg){

        this.port = port;
        this.qconnection = qconnection;
        this.msg = msg;

    }
    
    public void run(){
        try {

                String message = msg.getText(); // il messaggio ricevuto da STOMP è un TextMessage perchè ho settato auto_content_length=False per CONNECT
                
                System.out.println("[DISPATCHER_MSG_LISTENER] Messaggio ricevuto: " + message);
    
                System.out.println("[DISPATCHER_MSG_LISTENER] JMSReplyTo: " + msg.getJMSReplyTo());
                
                Queue qresponse = (Queue)msg.getJMSReplyTo();

                IService service_proxy = new ServiceProxy ("localhost", port); // creo un Proxy

                String result = null;

                if(message.equalsIgnoreCase("preleva")){
                
                    // invoca il DispatcherProxy che deve invocare il servizio di prelievo
                    System.out.println("[DISPATCHER_MSG_LISTENER] Ricevuta richiesta prelievo");
                    
                    int valore = service_proxy.preleva();

                    result = new String(Integer.toString(valore));
                    
                }
                else if(message.contains("deposita")){

                    // Deposito
                    String[] splitted = message.split("-");
                    Integer valoreDaDepositare = Integer.valueOf(splitted[1]);
                    System.out.println("[DISPATCHER_MSG_LISTENER] Ricevuta richiesta di deposito. Valore da depositare " + valoreDaDepositare );
                    
                    // invoca il DispatcherProxy che deve invocare il servizio di deposito
                    service_proxy.deposita(valoreDaDepositare);

                    result = new String("deposited");
                }

                // rispondo tramite JMS al client Python
			    QueueSession qsession = qconnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
			    TextMessage response_message = qsession.createTextMessage(result);
			    QueueSender sender = qsession.createSender(qresponse);
			    sender.send(response_message);

                sender.close();
                qsession.close();

            } catch (JMSException e) {
                e.printStackTrace();
        }
    }
}
