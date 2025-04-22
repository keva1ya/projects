#include <stdio.h>
int main(){
int a,b;
printf("Enter the number you want the factorial of:");
scanf("%d",&a);
for (b=1;a>1; a--)
{
    b=b*a;


printf("The value of the factorial is %d",b);

}