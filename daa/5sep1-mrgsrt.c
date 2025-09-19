#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void mergesort(int a[], int lidx, int ridx) {
    if (lidx >= ridx) return;
    int idx = (lidx + ridx) / 2;
    mergesort(a, lidx, idx);
    mergesort(a, idx + 1, ridx);
    int n1 = idx - lidx + 1, n2 = ridx - idx;
    int left[n1], right[n2];
    for (int i = 0; i < n1; i++) left[i] = a[lidx + i];
    for (int j = 0; j < n2; j++) right[j] = a[idx + 1 + j];
    int i = 0, j = 0, k = lidx;
    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            a[k++] = left[i++];
        } else {
            a[k++] = right[j++];
        }
    }
    while (i < n1) a[k++] = left[i++];
    while (j < n2) a[k++] = right[j++];
}
int main() {
    int n, max;
    printf("enter number of elements- ");
    scanf("%d", &n);
    printf("enter max value- ");
    scanf("%d", &max);
    int a[n];
    srand(time(NULL));
    for (int i = 0; i < n; i++) a[i] = rand() % max;
    printf("original array-\n");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    mergesort(a, 0, n - 1);
    printf("\n");
    printf("sorted array-\n");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}