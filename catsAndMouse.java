import java.util.*;
import java.io.*;

public class catsAndMouse{

  // static void findResult(List<Integer> a){
  //   int cata = a.get(0);
  //   int catb = a.get(1);
  //   int mouse = a.get(2);
  //   if(catb - mouse == mouse - cata){
  //     System.out.println("mouse C");
  //   }
  //   if(catb - mouse > mouse - cata){
  //     System.out.println("cat B");
  //   }
  //   else if(catb - mouse < mouse - cata){
  //     System.out.println("cat A");
  //   }
  // }

  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    List<Integer> li = new ArrayList<Integer>();
    for(int i = 0; i<n; i ++){
      String lines = br.readLine();
      String strs[] = lines.trim().split("");
      li.get(i) = strs[i];
    }

    // for(int )
    System.out.println(li.get(0));
  }
}
