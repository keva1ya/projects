#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int bubblesort(int a[], int x) {
    int y, z, tmp;
    for (y = 0; y < x - 1; y++) {
        for (z = 0; z < x - y - 1; z++) {
            if (a[z] > a[z + 1]) {
                tmp = a[z];
                a[z] = a[z + 1];
                a[z + 1] = tmp;
            }
        }
    }
    return 0;
}
int main() {
    int numbers[1000];
    int count;
    const int mxcount = 1000;
    const int mxrval = 1000;
    char filein[] = "random-numbers.txt";
    char fileout[] = "sorted-numbers.txt";
    while (1) {
        printf("enter quantity of random numbers (0<num<= 1k): ");
        scanf("%d", &count);
        if (count > 0 && count <= mxcount) {
            break;
        } else {
            printf("please enter a number between 1 and 1k.\n");
        }
    }
    FILE *f = fopen(filein, "w");
    if (f == NULL) {
        printf("input file (%s) couldn't be opened for writing\n", filein);
        return 1;
    }
    srand(time(NULL));
    for (int i = 0; i < count; i++) {
        numbers[i] = rand() % mxrval;
        fprintf(f, "%d\n", numbers[i]);
    }
    fclose(f);
    printf("random numbers written to %s\n", filein);
    bubblesort(numbers, count);
    f = fopen(fileout, "w");
    if (f == NULL) {
        printf("failed to open output file (%s) for writing\n", fileout);
        return 1;
    }
    for (int i = 0; i < count; i++) {
        fprintf(f, "%d\n", numbers[i]);
    }
    fclose(f);
    printf("random numbers in ascending order entered into %s\n", fileout);
    return 0;
}