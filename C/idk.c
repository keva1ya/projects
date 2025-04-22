#include<stdio.h>
void main () {
int a[5], l, l2, x ;
for (int i = 0; i < 5; i++)
{
    printf("Enter Integer No. %d: ", i+1, a[i]);    
        scanf("%d",&a[i]);
    }
       l=0;
       
       for (int i = 0; i<5; i++)
       {
        if (l<a[i])
        {
            l=a[i];
            x=i;
        }
        l2=0;
        for (int i=0; i<5; i++)
        if (i==x)
        {
            i++;
            i--;
        }
        else
        {
            if (l2<a[i])
            l2=a[i];
        }
       }
       printf("The 2nd largest integer is %d \n",l2);
       printf ("The Largest integer is %d \n", l);   
}