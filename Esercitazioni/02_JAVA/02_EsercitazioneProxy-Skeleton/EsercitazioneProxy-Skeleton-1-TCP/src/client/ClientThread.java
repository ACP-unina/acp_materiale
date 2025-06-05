package client;

import java.util.Random;

public class ClientThread extends Thread {

    private DispatcherProxy proxy;

    private static final int NUM_REQS = 3;


    public ClientThread(String ip_address, int port){

        proxy = new DispatcherProxy(ip_address, port);

        
    }

    public void run(){

        Random rand = new Random();

        for (int i = 0; i < NUM_REQS; i++){

            int waiting_time = rand.nextInt(3) + 2;

            try {

                Thread.sleep(waiting_time * 1000);

            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }


            int command = rand.nextInt(4);

            System.out.println("[CLIENT THREAD] Sending command " + command);

            proxy.sendCmd(command);


        }


    }

}
