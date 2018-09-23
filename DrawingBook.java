import java.util.*;
import java.io.*;

public class DrawingBook{

  static int frontTraverse(int result){
    // int fptr = 1;
    // int countf = 0;
    // if(res == fptr){
    //     break;
    // }
    // else{
    //   count += 1;
    //   while(fptr <= n){
    //     fptr = fptr + 2;
    //     if(fptr - 1 == res || fptr == res ){
    //       break;
    //     }
    //     else{
    //       countf += 1;
    //     }
    //   }
    // }
    return result/2;
  }

  static int backTraverse(int result, int total){
    int fptr = total;
    int countb = 0;
    if(fptr == result){
      return 0;
    }
    else{
      if(total % 2 == 0){
        // if(result == fptr){
        //   break;
        // }
        countb += 1;
        while(fptr >= 1){
          fptr = fptr - 2;
          if(fptr + 1 == result || fptr == result){
            break;
          }
          else{
            countb += 1;
          }
        }
      }

      else{
        while(fptr >= 1){
          if(fptr - 1 == result || fptr == result){
            break;
          }
          else{
            fptr = fptr - 2;
            countb += 1;
          }
        }
      }
    }
    return countb;
  }

  static int min(int a,int b){
    if(a < b){
      return a;
    }
    else{
      return b;
    }
  }

  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    // String lines = br.readLine();
    // String[] strs = lines.trim().split(" ");
    // List<Integer> a = new ArrayList<Integer>();
    // for(int i=0; i<n;i++) {
    // 	a.add(Integer.parseInt(strs[i]));
    // }
    int res = Integer.parseInt(br.readLine());
    int front = frontTraverse(res);
    int back = backTraverse(res, n);
    System.out.println(min(front, back));
  }
}
