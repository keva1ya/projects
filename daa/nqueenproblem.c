#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int N;
int **board;
bool isSafe(int row, int col) {
    int i, j;
    for (i = 0; i < col; i++)
        if (board[row][i])
            return false;
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;

    return true;
}
bool solveNQ(int col) {
    if (col == N)
        return true;
    for (int row = 0; row < N; row++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;

            if (solveNQ(col + 1))
                return true;

            board[row][col] = 0;
        }
    }
    return false;
}
void printBoard() {
    printf("Solution for N=%d:\n", N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%c ", board[i][j] ? '1' : '.');
        printf("\n");
    }

    printf("Queen positions (row,column) 1-based:\n");
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            if (board[i][j]) {
                printf("(%d,%d)", i+1, j+1);
                if (j < N-1) printf(", ");
                break;
            }
        }
    }
    printf("\n");
}
int main() {
    printf("Enter number of queens (N): ");
    if (scanf("%d", &N) != 1) {
        fprintf(stderr, "Invalid input\n");
        return 1;
    }
    if (N <= 0) {
        fprintf(stderr, "N must be positive\n");
        return 1;
    }
    board = malloc(N * sizeof(int*));
    if (!board) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }
    for (int i = 0; i < N; i++) {
        board[i] = malloc(N * sizeof(int));
        if (!board[i]) {
            fprintf(stderr, "Memory allocation failed\n");
            for (int r = 0; r < i; r++) free(board[r]);
            free(board);
            return 1;
        }
    }
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            board[i][j] = 0;
    if (solveNQ(0))
        printBoard();
    else
        printf("No solution found\n");
    for (int i = 0; i < N; i++) free(board[i]);
    free(board);
    return 0;
}