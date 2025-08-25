#include <stdio.h>
#include <stdlib.h>

int insertionsort(int a[], int x) {
    int y, z, tmp;
    for (y = 1; y < x; y++) {
        tmp = a[y];
        z = y - 1;
        while (z >= 0 && a[z] > tmp) {
            a[z + 1] = a[z];
            z--;
        }
        a[z + 1] = tmp;
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
        printf("Enter quantity of numbers to read (0 < num <= 1k): ");
        if (scanf("%d", &count) != 1) {
            while (getchar() != '\n');
            continue;
        }
        if (count > 0 && count <= mxcount) break;
        else printf("Please enter a number between 1 and 1000.\n");
    }
    FILE *f = fopen(filein, "r");
    if (f == NULL) {
        printf("Input file (%s) couldn't be opened for reading\n", filein);
        return 1;
    }
    int idx = 0;
    while (idx < count && fscanf(f, "%d", &numbers[idx]) == 1) {
        idx++;
    }
    fclose(f);
    insertionsort(numbers, idx);
    f = fopen(fileout, "w");
    if (f == NULL) {
        printf("Failed to open output file (%s) for writing\n", fileout);
        return 1;
    }
    for (int i = 0; i < idx; i++) {
        fprintf(f, "%d\n", numbers[i]);
    }
    fclose(f);
    printf("Numbers sorted and written to %s\n", fileout);
    return 0;
}
