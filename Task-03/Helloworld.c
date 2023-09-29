#include<stdio.h>
int main() {
        int n,i,j,c=0;
        printf("enter the number");
        scanf("%d",&n);
        for(i=2;i<=n;i++){
            c=0;
            for (j=2;j<i;j++){
                if (i%j==0){
                    c=1;
                    break;
                    }
            }
        
        if (c==0){
            printf("%d",i);
            printf(" ");
            }
    }
    
 return 0;

}