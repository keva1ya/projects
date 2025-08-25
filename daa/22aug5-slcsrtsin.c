#include <stdio.h>
#include <stdlib.h>

int selectionsort(int a[], int x) {
    int y, z, minid, tmp;
    for (y = 0; y < x - 1; y++) {
        minid = y;
        for (z = y + 1; z < x; z++) {
            if (a[z] < a[minid]) {
                minid = z;
            }
        }
        tmp = a[minid];
        a[minid] = a[y];
        a[y] = tmp;
    }
    return 0;
}
int main() {
    int numbers[1000];
    int count;
    const int mxcount = 1000;
    char filein[] = "ascending-numbers.txt";
    char fileout[] = "sorted-numbers.txt";
    while (1) {
        printf("enter quantity of numbers (0 < num <= 1k): ");
        if (scanf("%d", &count) != 1) {
            while (getchar() != '\n');
            continue;
        }
        if (count > 0 && count <= mxcount) break;
        else printf("Please enter a number between 1 and 1k.\n");
    }
    FILE *f = fopen(filein, "w");
    if (f == NULL) {
        printf("input file couldnt be opened for writing\n", filein);
        return 1;
    }
    for (int i = 0; i < count; i++) {
        numbers[i] = i + 1;  
        fprintf(f, "%d\n", numbers[i]);
    }
    fclose(f);
    f = fopen(filein, "r");
    if (f == NULL) {
        printf("Input file couldn't be opened for reading\n", filein);
        return 1;
    }
    int idx = 0;
    while (idx < count && fscanf(f, "%d", &numbers[idx]) == 1) {
        idx++;
    }
    fclose(f);
    selectionsort(numbers, count);
    f = fopen(fileout, "w");
    if (f == NULL) {
        printf("Failed to open output file for writing\n", fileout);
        return 1;
    }
    for (int i = 0; i < count; i++) {
        fprintf(f, "%d\n", numbers[i]);
    }
    fclose(f);
    printf("Numbers in ascending order written \n", fileout);
    return 0;
}
