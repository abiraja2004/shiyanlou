public class ShiyanlouImpl implements Shiyanlou{
    @Override
    public String toUp(String s) {
        if(null ==s){
          return null;
        }
      
        return s.toUpperCase();
    }
}
