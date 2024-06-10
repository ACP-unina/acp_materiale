package threadpipe;

import java.io.PipedOutputStream;

public class Test {
	
	public static void main(String[] args)  {
		// TODO Auto-generated method stub
	
		// A piped output stream can be connected to a piped input stream to create a communications pipe.
		PipedOutputStream pipeOut = new PipedOutputStream();
		
		WriterThread w = new WriterThread (pipeOut);
		ReaderThread r = new ReaderThread (pipeOut);
		
		w.start();
		r.start();
		
		
	}

}
