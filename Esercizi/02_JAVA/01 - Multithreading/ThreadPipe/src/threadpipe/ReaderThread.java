package threadpipe;

import java.io.*;

/*
 * ReaderThread: legge il contenuto 
 * della pipe
 */


public class ReaderThread extends Thread {
	
	private DataInputStream dataIn; 
	
	public ReaderThread ( PipedOutputStream pipeOut ){
		
		try{
			
			// crea un PipedInputStream collegato al PipedOutputStream
			// utilizzato in output dal thread Writer
			
			dataIn = new DataInputStream ( new PipedInputStream ( pipeOut )  ) ;
		}catch ( IOException e ){
			e.printStackTrace();
		}
		
		
	}
	
	
	public void run (){
		
		String s;
		
		while ( true ){
			
			try{
				System.out.println ( "						[READER] waiting for new input ... " );
				// input da pipe
				s= dataIn.readUTF() ;
				System.out.println ( "						[READER] input form pipe: " + s );
			}catch ( IOException e ){
				e.printStackTrace();
			}
		}
		
	}

}
