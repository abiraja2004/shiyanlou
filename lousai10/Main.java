import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class Main {
    // TODO
    public static void  ioc(String className,Shiyanlou s,String methodName, String name){
      try{ 
        Class<?> clazz = Class.forName(className);
        Object instance = clazz.newInstance();
        Field[] fields = instance.getClass().getDeclaredFields();
        for(Field field : fields){
          String shiyanlou = field.getGenericType().toString();
          if("interface Shiyanlou".equals(shiyanlou)){
            String setMethod = "set"+field.getName().substring(0,1).toUpperCase()+field.getName().substring(1);
            Method method1 = instance.getClass().getMethod(setMethod,Shiyanlou.class);
            method1.invoke(instance,s);
          }
        }
        Method method2 = instance.getClass().getMethod(methodName,String.class);
        method2.invoke(instance,name);
      }catch(Exception e){}
   }
}
