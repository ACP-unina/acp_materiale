package prodcons1b;

import java.io.*;

public class Test {

	/**
	 * @param args
	 */
	public static void main(String[] args)  {
		// TODO Auto-generated method stub

		
		// * creazione del buffer condiviso * 
		Buffer buf = new Buffer();

			
		BufferedReader stdin = new BufferedReader( new InputStreamReader ( System.in ) ); 
		int choice=0, id=1;
		
		while ( true ){
			System.out.println ( "0 (C) /1 (P) >> " );
			
			try{
				
				// * input da tastiera  * 
				choice =   Integer.parseInt( stdin.readLine());
				
			}catch( IOException e){e.printStackTrace();}
			
			if ( choice == 0){
				Consumer c = new Consumer(buf, "		consumer_" + id );
				c.start();
			}
			else{
				Producer p = new Producer( buf, "								producer_" + id );
				p.start();
				
			}	
			
			id=id+1;
			
		}
		
		
		
	}

}