package threadpipe;

import java.io.*;

/*
 * WriterThread: legge una stringa da System.in e 
 * fa output sulla pipe
 */

public class WriterThread extends Thread {
	
	private DataOutputStream dataOut;
	
	
	public WriterThread ( PipedOutputStream pipeOut ){
		dataOut  = new DataOutputStream ( pipeOut );
		
	}
	
	
	public void run (){
		
		// BufferedReader per lettura da System.in
		BufferedReader keyboardBuf = new BufferedReader ( new InputStreamReader ( System.in ) );
		String s;
		
		while ( true ){
			try{
				System.out.println ( "[Writer] enter string: "  );
				
				// lettura stringa
				s = keyboardBuf.readLine();
				System.out.println ( "[Writer] string: < " + s  + " > output to pipe");

				// output su pipe
				dataOut.writeUTF(s);
				
			}catch ( IOException e ){
				e.printStackTrace();
			}
		}	
	}

}
