package tools;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * 
 * @author 
 *
 */
public class CsvTools {
	


	/**
	 * 读取csv文件
	 * @param csvfile csv文件路径
	 * @param lines 读取指定行数
	 * @param offset 开始行数
	 * @param sign 分隔符
	 * @return List<List>
	 */
	public static List<List<String>> csvReader(String csvfile,int lines,int offset,String sign){
		
		List<List<String>> csvList = new ArrayList<List<String>>();
		
		File filepath = new File(csvfile);
		//判断文件是否存在
		if(!filepath.exists()){
			return null;
		}
		int i = 0;
		int j = 0;
		//流读取
		BufferedReader br = null;
		try {
			br = new BufferedReader(new FileReader(filepath));
			
			String line = "";
			while((line=br.readLine()) != null){
				i++;
				if(i<offset){
					continue;
				}
				
				if(j<lines){
					j++;
					String[] st = line.split(sign);
					List<String> list = new ArrayList<String>();
					for(String t : st){
						list.add(t);
					}
					csvList.add(list);
				}
				
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally{
			try {
				br.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		return csvList;
	} 
}
