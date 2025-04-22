#include <stdio.h>
int gcd(int n1, int n2)
{ 
    int j;
    if (n1>n2)
    j=n1;
    else{j=n2;}

    int gcd;
    for(int i=1; i<=j; i++)
    {
        if(n1%i==0 && n2%i==0)
        {
            gcd = i;
        }
    }
    return gcd;
}
int main ()
{
    int a,b;
    printf("Enter Two Numbers:");
    scanf("%d %d",&a,&b);
    printf("G.C.D.of %d and %d is : %d ",a, b, gcd(a,b));
}