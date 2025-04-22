#include <stdio.h>
int main() {
int ar[] = {10, 20, 30, 40, 50};
int k = sizeof(ar) / sizeof(ar[0]);
printf("Original array: ");
for (int i = 0; i < k; i++) {
printf("%d ", ar[i]);
}
printf("\n");
for (int i = 1; i < k - 1; i++) {
ar[i] = ar[i + 1];
}
k--;
printf("Array after deleting the second element: ");
for (int i = 0; i < k; i++) {
printf("%d ", ar[i]);
}
printf("\n");
return 0;
}