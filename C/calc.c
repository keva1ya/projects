#include<stdio.h>
int main ()
{
    int n, n1, n2,k ;
    printf("Choose The action you want to perform \n For Multiplication type 1\n For Division type 2 \n For Addition type 3 \n For Subtraction type 4\n Select Function: ");
    scanf ("%d", &n);
    printf("Enter No.1:");
    scanf("%d", &n1);
    printf("Enter No.2:");
    scanf("%d",&n2);
    if (n==1)
    {
       k= n1 *n2;
       printf("The Product of the numbers is %d \n ",k);
    }
    if (n==2)
    {
        k= n1 / n2;
        printf("The Value of No.1/No.2 is %d",k);
    }
    if (n==3)
    {
        k= n1 + n2;
        printf("The sum of the numbers is %d",k);
    }
    if (n==4)
    {
        k= n1-n2;
        printf("The difference between the numbers is %d",k);
    }
}