#include <stdio.h>
int main ()
 {
    int num1, num2 ,sum ;
printf ("enter number 1:");
scanf ("%d", &num1);
printf ("enter number 2: ");
scanf ("%d", &num2);
sum = num1 + num2 ;
if (num1 == 10 && num2 == 9 || num1 == 9 && num2 == 10  )
printf ("tweny one \n");

else printf ("The sum of %d and %d is %d \n", num1,num2,sum);

return 0 ;
}