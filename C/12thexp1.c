#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    char filename[] = "kali.txt";
    char text[] = "hello ebherynyan\n";


    fp = fopen(filename, "a");


    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }


    fprintf(fp, "%s", text);

    fclose(fp);

    printf("File created and text entered \n");

    return 0;
}