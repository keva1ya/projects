#include <stdio.h>

int main() {
    int num=50, shift=5,lshift,rshift;
    
    lshift = num << shift;
    printf("Left Shift %d\n",lshift);

   
    rshift = num >> shift;
    printf("Right Shift %d\n",rshift);

    return 0;
}