#include <stdio.h>

int main() {
    int 
    num1=20,
    num2=15,
    shift=2,
    and,or,not1,not2,lshift,rshift ;  

    
    and = num1 & num2;
    printf("Bitwise AND: %u\n", and); 

    
    or = num1 | num2;
    printf("Bitwise OR: %u\n", or); 

    
    not1 = ~num1;
    not2 = ~num2;
    printf("Bitwise NOT of num1: %u\n", not1);
    printf("Bitwise NOT of num2: %u\n", not2); 

    lshift = num1 << shift;
    printf("Left Shift %d\n",lshift);

   
    rshift = num1 >> shift;
    printf("Right Shift %d\n",rshift);

    return 0;
}