import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

class FileOperate{
	public String readFile(String pathName){
		StringBuffer buffer = new StringBuffer();
		File file = new File(pathName);
		BufferedReader br=null;
		try {
			br = new BufferedReader(new FileReader(file));
			String str = null;
			int i=0;
			while((str=br.readLine()) != null){
				if( i!=0){
					buffer.append(" ");
				}
				buffer.append(str);
				i++;
			}
		} catch (Exception e) {
		}finally{
			if(br!=null){
				try {
					br.close();
				} catch (IOException e) {
					
				}
			}
		}
		return buffer.toString();
	}
	
	public void outFile(String pathName,String result){
		File file = new File(pathName);
		BufferedWriter bw = null;
		try{
			bw = new BufferedWriter(new FileWriter(file));
			bw.write(result);
		} catch (IOException e) {
			
		}finally{
			if(bw!=null){
				try {
					bw.close();
				} catch (IOException e) {
					
				}
			}
		}
	}
}