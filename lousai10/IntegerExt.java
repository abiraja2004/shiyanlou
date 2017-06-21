

public class IntegerExt {
    private int i;
    private IntegerExt(int i){
        this.i = i;
    }
    public int toIntValue(){
        return i;
    }
    public static IntegerExt getInstance(int i){

    	if (i >= IntCache.low && i <= IntCache.high)
            return IntCache.cache[i + (-IntCache.low)];
        return new IntegerExt(i);
        
    }
    
    private static class IntCache {
        static final int low = -128;
        static final int high;
        static final IntegerExt cache[];

        static {
            // high value may be configured by property
            int h = 127;
            
            high = h;

            cache = new IntegerExt[(high - low) + 1];
            int j = low;
            for(int k = 0; k < cache.length; k++)
                cache[k] = new IntegerExt(j++);

            // range [-128, 127] must be interned (JLS7 5.1.7)
            assert IntCache.high >= 127;
        }

        private IntCache() {}
    }
    
    public static void main(String[] args) {
    	IntegerExt i1 = IntegerExt.getInstance(1);
    	IntegerExt i2 = IntegerExt.getInstance(1);
    	IntegerExt i3 = IntegerExt.getInstance(1111);
    	IntegerExt i4 = IntegerExt.getInstance(1111);
    	System.out.println(i1 == i2);
    	System.out.println(i1.equals(i2));
    	System.out.println(i3 == i4);
    	System.out.println(i3.equals(i4));
    	
	}
    public boolean equals(Object obj) {
        if (obj instanceof IntegerExt) {
            return i == ((IntegerExt)obj).toIntValue();
        }
        return false;
    }
	
}


















