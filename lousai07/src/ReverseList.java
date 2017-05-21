import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

class ReverseList<T> extends ArrayList<T>{

	private static final long serialVersionUID = 1L;
	
	public ReverseList(Collection<T> c){ super(c);}
	
	public Iterable<T> reversed(){
		return new Iterable<T>() {

			@Override
			public Iterator<T> iterator() {
				
				return new Iterator<T>() {
					int cursor = ReverseList.this.size();
					
					@Override
					public boolean hasNext() {	
						return cursor != 0;
					}

					@Override
					public T next() {
//						int i = cursor-1;
//	                    Object[] elementData = ReverseList.this.toArray();
//	                    cursor = i ;
	                    return get(--cursor);
					}
				};
			}
		};
	}
}
