public class StringUtils {
    public static boolean allIsNotNull(String... s){
        // TODO
        if(s == null || s.length == 0){
          return false;
        }
        for(int i =0; i<s.length;i++){
          if(null == s[i]){
            return false; 
          } 
        }
        return true;
    }

    public static boolean allIsNotEmpty(String... s){
        // TODO
        if(s == null || s.length == 0){
          return false;
        }
        for(int i=0; i<s.length;i++){
          if( null==s[i] || "".equals(s[i])){
             return false;
          }
        }
        return true;
    }
}
