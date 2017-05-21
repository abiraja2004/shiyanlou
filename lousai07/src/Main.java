import java.io.File;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class Main {
	public static void main(String[] args) {
		fileOp();
	}
	public static void fileOp(){
		FileOperate fo = new FileOperate();
		String in = "d:"+File.separator+"words.txt";
//		fo.readFile(in);
		String out = "d:"+File.separator+"out.txt";
//		fo.outFile(out, fo.readFile(in));
		String re = fo.readFile(in);
//		String[] res = re.split(" ");
//		
//		ReverseList<String> rl = new ReverseList<String>(Arrays.asList(res));
//		StringBuffer buf = new StringBuffer();
//		Iterator<String> it = rl.reversed().iterator();
//		int i=0;
//		while(it.hasNext()){
//			if(i!=0){
//				buf.append(" ");
//			}
//			buf.append(it.next());
//			i++;
//		}
		
		
		fo.outFile(out, re);
	}
	
	public static void cp(){
		BlockingQueue<String> queue = new LinkedBlockingQueue<String>(10);
		Consumer c = new Consumer(queue);
		Producer p = new Producer(queue);
		new Thread(c).start();
		new Thread(p).start();
	}
}
