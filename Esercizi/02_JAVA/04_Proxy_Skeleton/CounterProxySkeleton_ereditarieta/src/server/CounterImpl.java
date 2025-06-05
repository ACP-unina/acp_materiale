package server;


//CASO 2: implementazione per delega, CounterImpl has-a CounterSkel
//import service.*;
//
//public class CounterImpl implements ICounter {

//CASO 1: implementazione per ereditarieta', CounterImpl is-a CounterSkel
public class CounterImpl extends CounterSkel {

	private int count;
	
	public CounterImpl() {
		count = 0;
	}
	
	public int get() {
		return count;
	}

	
	public synchronized void inc() {
		count++;
	}

	
	public synchronized void sum (int value)  {
		count += value;
	}
	
	public  synchronized void square(){
		count=count*count;
	}
	
}