#include <stdio.h>
#include <limits.h>

#define MAX 20
#define MAXN 50

int dp[MAX][MAX], bracket[MAX][MAX];
int p[MAX];
int A[MAX][MAXN][MAXN];
int result[MAXN][MAXN];

void multiply(int A[MAXN][MAXN], int B[MAXN][MAXN], int C[MAXN][MAXN], int r1, int c1, int c2) {
    for (int i = 0; i < r1; i++)
        for (int j = 0; j < c2; j++) {
            C[i][j] = 0;
            for (int k = 0; k < c1; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
}

void multiplication(int i, int j, int res[MAXN][MAXN]) {
    if (i == j) {
        for (int r = 0; r < p[i-1]; r++)
            for (int c = 0; c < p[i]; c++)
                res[r][c] = A[i][r][c];
        return;
    }
    int left[MAXN][MAXN], right[MAXN][MAXN];
    multiplication(i, bracket[i][j], left);
    multiplication(bracket[i][j] + 1, j, right);
    multiply(left, right, res, p[i-1], p[bracket[i][j]], p[j]);
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i <= n; i++) scanf("%d", &p[i]);

    for (int k = 1; k <= n; k++)
        for (int i = 0; i < p[k-1]; i++)
            for (int j = 0; j < p[k]; j++)
                scanf("%d", &A[k][i][j]);

    for (int i = 1; i <= n; i++) dp[i][i] = 0;
    for (int L = 2; L <= n; L++)
        for (int i = 1; i <= n - L + 1; i++) {
            int j = i + L - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j];
                if (cost < dp[i][j]) {
                    dp[i][j] = cost;
                    bracket[i][j] = k;
                }
            }
        }

    multiplication(1, n, result);

    for (int i = 0; i < p[0]; i++) {
        for (int j = 0; j < p[n]; j++)
            printf("%4d ", result[i][j]);
        printf("\n");
    }

    return 0;
}
