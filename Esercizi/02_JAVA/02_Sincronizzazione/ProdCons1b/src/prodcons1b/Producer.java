package prodcons1b;

public class Producer extends Thread {

	private Buffer buffer;
	
	
	public Producer ( Buffer b, String name ){
		super ( name );
		buffer=b;
	}
	
	
	public void run (){
		buffer.produci();
	}

	
}