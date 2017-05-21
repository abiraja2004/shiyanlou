import java.util.concurrent.BlockingQueue;

class Consumer implements Runnable {
	private final BlockingQueue<String> queue;
	Consumer(BlockingQueue<String>queue){
		this.queue=queue;
	}
	@Override
	public void run() {
		int i = 1;
		while (true) {
			try {
				
				System.out.println("Complete consumption:Course"+queue.take());
				Thread.sleep(100);
				i++;
				if (i == 11) {
					break;
				}
			} catch (InterruptedException e) {

				e.printStackTrace();

			}

		}
	}

}
