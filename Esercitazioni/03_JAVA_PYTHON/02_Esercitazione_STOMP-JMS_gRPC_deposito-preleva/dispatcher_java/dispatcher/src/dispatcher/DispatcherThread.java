package dispatcher;

import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.jms.TextMessage;

import io.grpc.StatusRuntimeException;

public class DispatcherThread extends Thread{

    private MagazzinoGrpc.MagazzinoBlockingStub blockingStub;
    private QueueConnection qconnection;
    private TextMessage msg;
  
    public DispatcherThread(MagazzinoGrpc.MagazzinoBlockingStub blockingStub, QueueConnection qconnection, TextMessage msg){

        this.blockingStub = blockingStub;
        this.qconnection = qconnection;
        this.msg = msg;

    }
    
    public void run(){
        try {

                String message = msg.getText(); // il messaggio ricevuto da STOMP è un TextMessage perchè ho settato auto_content_length=False per CONNECT
                
                System.out.println("[DISPATCHER_MSG_LISTENER] Messaggio ricevuto: " + message);
    
                System.out.println("[DISPATCHER_MSG_LISTENER] JMSReplyTo: " + msg.getJMSReplyTo());
                
                Queue qresponse = (Queue)msg.getJMSReplyTo();

                String result = null;

                // Preleva tramite RPC JAVA preleva
                if(message.equalsIgnoreCase("preleva")){
                

                    System.out.println("[DISPATCHER_MSG_LISTENER] Ricevuta richiesta prelievo");
                    
                    Empty empty = Empty.newBuilder().build();
                    Articolo articolo = null;
                    try {
                        articolo = blockingStub.preleva(empty);
                        result = new String(Long.toString(articolo.getValore()));
                    } catch (StatusRuntimeException e) {
                        System.out.println("RPC failed: {0} " + e.getStatus());
                        result = new String("-1");
                        
                    }

                    
                    
                }
                else if(message.contains("deposita")){

                    // Deposito tramite RPC JAVA deposita
                    String[] splitted = message.split("-");
                    Integer valoreDaDepositare = Integer.valueOf(splitted[1]);
                    System.out.println("[DISPATCHER_MSG_LISTENER] Ricevuta richiesta di deposito. Valore da depositare " + valoreDaDepositare );
                    
                    
                    Articolo articolo = Articolo.newBuilder().setValore(valoreDaDepositare).build();

                    try {
                        blockingStub.deposita(articolo);
                        result = new String("deposited");
                    } catch (StatusRuntimeException e) {
                        System.out.println("RPC failed: {0} " + e.getStatus());
                        result = new String("not deposited");
                        
                    }

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
