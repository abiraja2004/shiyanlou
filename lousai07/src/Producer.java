import java.util.concurrent.BlockingQueue;

class Producer implements Runnable {
	private final BlockingQueue<String> queue;

	Producer(BlockingQueue<String> queue) {
		this.queue = queue;
	}

	@Override
	public void run() {
		int i = 1;
		while (true) {
			try {
				System.out.println("Complete production:Course" + i);
				queue.put("" + i);
				Thread.sleep(1);
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
