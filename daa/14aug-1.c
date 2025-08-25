#include <stdio.h>
int bubblesort(int a[],int x)
{
int y,z, tmp;
for (y=0; y<x-1; y++){
    for (z=0, z<x-y-1; z++;){
        if (a[z] > a[z+1]) {
            tmp = a[z];
            a[z] = a[z+1];
            a[z+1] = tmp;
        }
    }
    }
    return 0;
}
int main(){
    int x;
    printf("enter quantity of numbers to be entered:");
    scanf("%d", &x);
    int a[x];
    for (int i = 0; i < x; i++) {
        printf("enter the number:");
        scanf("%d", &a[i]);
    }
bubblesort(a, x);
    printf("sorted numbers (in ascending order) are:");
    for (int i = 0; i < x; i++) {
        printf("%d ", a[i]);
    }
    return 0;
}