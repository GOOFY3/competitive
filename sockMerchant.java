import java.io.*;
import java.util.*;

public class sockMerchant{

  static int count(int n, List<Integer> myList){
    int cnt = 0;
    for(int i=0; i<myList.size(); i++){
      if(myList.get(i) == n){
        cnt = cnt + 1;
      }
    }
    // System.out.println(cnt);
    return cnt;
  }

  public static void main(String args[]) throws IOException{
    //read from keyboard
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    String  lines = br.readLine();


    String[] strs = lines.trim().split(" ");
    List<Integer> a = new ArrayList<Integer>();
    List<Integer> b = new ArrayList<Integer>();
    int res = 0;
    

    //parse input string
    for(int i=0; i<n;i++) {
    	a.add(Integer.parseInt(strs[i]));
    }

    //logic
    for(int i=0; i<a.size(); i++){
      if(!(b.contains(a.get(i)))){
        int count = count(a.get(i), a);
        // System.out.println(count);
        res = res + count/2;
        b.add(a.get(i));
      }
      else{
        continue;
      }
    }


    //print out pairs
    System.out.println(res);
  }
}
