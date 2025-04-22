#include<stdio.h>
 int GCD(int n ){
    int o,i,k,x;
    int j[o];

    for(i=1;i<=n;i++){
    if (n % i  == 0)
    { for(o=0;o>=0;o++){
      i=j[o];}
    }}
    for (;o>=0;o++)
       {
        if (x<j[o])
        {
            x=j[o];   
        }
       }
       return x;

 }

int main()
{
int a,b,c,d,x ;
printf("Enter first number:");
scanf("%d",&a);
printf("enter second number:");
scanf("%d",&b);
GCD(a),&c;
GCD(b),&d;

if (d<c) {x=c;}
else {x=d;}


printf("The greatest common divisor of the numbers%d & %d is %d", a,b,x);

}