import java.io.*;
import java.util.*;

public class sockMerchant{
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    String  lines = br.readLine();


    String[] strs = lines.trim().split(" ");
    List<Integer> a = new ArrayList<Integer>();
    int res = 0;


    //parse input string
    for(int i=0; i<n;i++){
      a.add(Integer.parseInt(strs[i]));
    }

    for(int i=0; i< a.size(); i++){
      int count = 0;
      for(int j=0;j<a.size();j++){
        if(a.get((i))==a.get((j))){
          count += 1;
          a.remove(a.get((j)));
          System.out.println(a);
        }
        else continue;

        if(count > 1){
          res = res + count/2;
        }
      }
    }

    //print out pairs
    System.out.println(res);
  }
}
