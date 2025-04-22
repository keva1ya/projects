#include <stdio.h>
int main() {
 int ar[] = {1, 2, 3, 4, 5};
 int size = sizeof(ar) / sizeof(ar[0]);
 for (int i = 0; i < size; i++) {
 printf("%d ", ar[i]);
 }
 printf("\n");
 return 0;
}