#include<stdio.h>
int main ()
{
    float a, b, c ;
    printf ("Please enter the length of all sides(use spaces between values):");
    scanf ("%d %d %d", &a, &b, &c);
    if ( ((a+b)>c) && ((b+c)>a) && ((a+c)>b) )
    {
        if(a==b && b==c)
        printf ("The triangle is equilateral");
        else if (a==b || b==c || a==c)
        printf ("The triangle is isoceles"); 
        else
        printf ("The triangle is scalene");
    }
    else
    printf(" These values of sides of Triangle do not form a trangle. ");
    return 0;
}