#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int divide(int arr[], int fir, int las) {
    int mid = (fir + las) / 2;
    int pivot = arr[mid];
    int tmp = arr[mid];
    arr[mid] = arr[las];
    arr[las] = tmp;
    int i = fir - 1;
    for (int j = fir; j < las; j++) {
        if (arr[j] <= pivot) {
            i++;
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
    tmp = arr[i + 1];
    arr[i + 1] = arr[las];
    arr[las] = tmp;
    return i + 1;
}
void quicksort (int arr[], int fir, int las) {
    if (fir < las) {
        int pi = divide(arr, fir, las);
        quicksort(arr, fir, pi - 1);
        quicksort(arr, pi + 1, las);
    }
}
int main() {
    int n, min, max;
    printf("enter the number of elements: ");
    if (scanf("%d", &n) != 1 || n <= 0) return 0;
    printf("enter minimum value: ");
    scanf("%d", &min);
    printf("enter maximum value: ");
    scanf("%d", &max);
    int *arr = malloc(n * sizeof(int));
    if (!arr) return 0;
    srand((unsigned)time(NULL));
    for (int i = 0; i < n; i++) {
        arr[i] = (rand() % (max - min + 1)) + min;
    }
    printf("original array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    quicksort(arr, 0, n - 1);
    printf("sorted array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    free(arr);
    return 0;
}
