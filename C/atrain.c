#include <stdio.h>
int factorial(int a){
    int b=0,c=1;
    while(b<a){
        b=b+1;
        c=c*b;
    }
    return c;
}
int main(){
    int a;
    printf("enter any integer:");
    scanf("%d",&a);
    printf("the factorial of the given integer is:%d",factorial(a));
    return 0;
}