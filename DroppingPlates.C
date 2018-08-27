#include<stdio.h>

int main(){
  int i, j, t ;
  int a[10][2];
  scanf("%d", &t);
  for(i=0;i<t;i++){
    for(j=0; j<2; j++){
      scanf("%d", &a[i][j]);
    }
  }
}
