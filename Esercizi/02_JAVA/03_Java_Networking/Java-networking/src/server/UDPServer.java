package server;

import java.io.IOException;
import java.net.*;

public class UDPServer {
	
	public static void main ( String[] args ){
		
		try{
			
			/*
			 * Creazione socket e pacchetto UDP lato server
			 */
			
			DatagramSocket socket = new DatagramSocket ( 8050 );
			
			byte[] data = new byte[65508]; 
			DatagramPacket packet = new DatagramPacket ( data, data.length );
			
			System.out.println ("[Server]: attesa pacchetto UDP..." );
			socket.receive( packet );
			System.out.println ("[Server]: pacchetto ricevuto." );
			
			/*
			 * Lettura e stampa del contenuto del pacchetto
			 * NOTA: l'invocazione di .getLength restituisce la lunghezza
			 * effettiva del pacchetto.
			 */
		
			// quello che riceviamo nel pacchetto UDP sono byte...quindi dovrò 
			// creare una stringa a partire da questi byte per stampare il contenuto
			
			byte[] receivedData = packet.getData();
			     
			String s = new String ( receivedData, 0, packet.getLength() );
			System.out.println ("[Server]: contenuto pacchetto: " + s );

			/*
			 * Invio risposta al client
			 */
			
			s = "OK client, pacchetto ricevuto";
			
			/*
			 * NOTA: nella costruzione del pacchetto 'response', l'IP / porta del 
			 * destinatario (ossia il client) sono ottenuti dal pacchetto 'packet'
			 */
			DatagramPacket response = new DatagramPacket ( s.getBytes(), s.getBytes().length, packet.getAddress(), packet.getPort() );

			Thread.sleep( 5000 );
			
			
			System.out.println ("[Server]: invio pacchetto risposta..." );
			socket.send( response );
			System.out.println ("[Server]: pacchetto inviato." );

			socket.close();
			
		}catch ( SocketException e ){
			e.printStackTrace();
		}catch ( IOException e ){
			e.printStackTrace();
		}catch ( InterruptedException e ){
			e.printStackTrace();
		}
		
	}

}
