import java.util.*;
import java.io.*;

public class pickingNumbers{
  static String getlast(List<String> l){
    return l.get(l.size()- 1);
  }
  static int count(List<String> l){
    return l.size();
  }
  static int result(List<Integer> l, int r){
    r = l.get(0) - r;
    for(int i =0; i < l.size()-1; i++){
      if(l.get(i+1) - l.get(i) > r){
        r = l.get(i+1) - l.get(i);
      }
      else{
        continue;
      }
      // System.out.println(r);
    }
    System.out.println(r);
    return r;
  }
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String n = br.readLine();
    int count = Integer.parseInt(n);
    String lines = br.readLine();
    String[] strs = lines.trim().split(" ");
    List<String> a = new ArrayList<String>();
    List<Integer> f = new ArrayList<Integer>();
    List<String> set = new ArrayList<String>();
    int res = 0;
    for(int i=0; i<count;i++) {
    	a.add(strs[i]);
    }
    Collections.sort(a);
    for(int i =0; i<count; i++){
      set.add(a.get(i));
      for(int j=i+1; j< count; j++){
        // System.out.println("Last Element:" + Integer.parseInt(a.get(i)));
        if(Integer.parseInt(a.get(i)) - Integer.parseInt(a.get(j)) <= 1 && Integer.parseInt(a.get(i)) - Integer.parseInt(a.get(j)) >= -1){
          set.add(a.get(j));
        }
        else{
          continue;
        }
      }
      int ct = count(set);
      f.add(ct);
      // System.out.println(f);
    // System.out.println(res);
    }
    result(f, res);
  }
}
