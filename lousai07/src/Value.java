/**
 * 
 */

/**
 * <p>
 * Title:Value
 * </p>
 * <p>
 * Description:
 * </p>
 * 
 * @author:bao
 * @date:2017年5月21日上午10:30:33
 */
public class Value {
	public int i;
	public String s;

	public Value(int i, String s) {
		this.i = i;
		this.s = s;
	}

	public Value(String s, int i) {
		this.i = i;
		this.s = s;
	}

	public boolean equals(Object o) {
		if (this == o)
			return true;
		if ((o == null) || (o.getClass() != this.getClass()))
			return false;
		Value test = (Value) o;
		return i == test.i && (s == test.s || (s != null && s.equals(test.s)));
	}

	public int hashCode() {
		int hash = 7;
		hash = 31 * hash + i;
		hash = 31 * hash + (null == s ? 0 : s.hashCode());
		return hash;
	}
}
