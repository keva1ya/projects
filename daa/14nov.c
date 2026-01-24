#include <stdio.h>
#include <string.h>

int main() {
    char a[100], b[100];

    printf("Enter first string: ");
    fgets(a, sizeof(a), stdin);

    printf("Enter second string: ");
    fgets(b, sizeof(b), stdin);

    if (a[strlen(a) - 1] == '\n') 
    {a[strlen(a) - 1] = '\0';}
    if (b[strlen(b) - 1] == '\n') 
    {b[strlen(b) - 1] = '\0';}

    int n = strlen(a), m = strlen(b);
    int dpmtx[101][101];

    for (int i = 0; i <= n; i++) 
    {
        for (int j = 0; j <= m; j++)
        {
            if (i == 0 || j == 0)
                dpmtx[i][j] = 0;
            else if (a[i-1] == b[j-1])
                dpmtx[i][j] = dpmtx[i-1][j-1] + 1;
            else
                dpmtx[i][j] = dpmtx[i-1][j] > dpmtx[i][j-1] ? dpmtx[i-1][j] : dpmtx[i][j-1];
        }
    }

    int i = n, j = m, k = 0;
    char lcs[101];

    while (i > 0 && j > 0) {
        if (a[i-1] == b[j-1]) 
        {
            lcs[k++] = a[i-1];
            i--; j--;}
        else if (dpmtx[i-1][j] > dpmtx[i][j-1])
        i--;
        else
        j--;}

    lcs[k] = '\0';

    for (int x = 0; x < k/2; x++) {
        char t = lcs[x];
        lcs[x] = lcs[k-1-x];
        lcs[k-1-x] = t;
    }

    printf("LCS Length: %d\n", dpmtx[n][m]);
    printf("LCS: %s\n", lcs);

    return 0;
}