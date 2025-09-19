#include <stdio.h>
int main() {
    int m1, n1, m2, n2;
    printf("Enter rows and columns of first matrix: ");
    scanf("%d %d", &m1, &n1);
    printf("Enter rows and columns of second matrix: ");
    scanf("%d %d", &m2, &n2);
    if (n1 != m2) {
        printf("Matrix multiplication not possible! Columns of first matrix must equal rows of second matrix.\n");
        return 0;
    }
    int A[m1][n1], B[m2][n2], C[m1][n2];
    printf("\nenter elements of first matrix:\n");
    for (int i = 0; i < m1; i++)
        for (int j = 0; j < n1; j++)
            scanf("%d", &A[i][j]);
    printf("\nenter elements of second matrix:\n");
    for (int i = 0; i < m2; i++)
        for (int j = 0; j < n2; j++)
            scanf("%d", &B[i][j]);
    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n2; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n1; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    printf("\nresultant matrix:\n");
    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n2; j++) {
            printf("%4d ", C[i][j]);
        }
        printf("\n");
    }
    return 0;
}
