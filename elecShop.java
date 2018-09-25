import java.util.*;
import java.io.*;

public class elecShop{

  static int returnAnswer(List<Integer> k, List<Integer> u , int budget) throws IndexOutOfBoundsException{
    int larger = 0;
    for(int i=0; i<k.size(); i++){
        for(int j=0; j < u.size(); j++){
          int temp = k.get(i) + u.get(j);
          if(temp > larger && temp <= budget){
            larger = temp;
          }
        }
    }
    return larger;
  }

  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // int n = br.readLine();
    String lines = br.readLine();
    String[] strs = lines.trim().split(" ");
    List<Integer> a = new ArrayList<Integer>();
    List<Integer> keyboard = new ArrayList<Integer>();
    List<Integer> usb = new ArrayList<Integer>();
    for(int i=0; i<3;i++) {
    	a.add(Integer.parseInt(strs[i]));
    }
    int b = a.get(0);
    int n = a.get(1);
    int m = a.get(2);

    //input next line
    String lines2 = br.readLine();
    String[] strs2 = lines2.trim().split(" ");
    for(int i = 0; i<n; i++){
      keyboard.add(Integer.parseInt(strs2[i]));
    }

    //input next line
    String lines3 = br.readLine();
    String[] strs3 = lines3.trim().split(" ");
    for(int i = 0; i<m; i++){
      usb.add(Integer.parseInt(strs3[i]));
    }

    int result = returnAnswer(keyboard, usb, b);
    if(result == 0){
      System.out.println(-1);
    }
    else{
      System.out.println(result);
    }
  }
}
