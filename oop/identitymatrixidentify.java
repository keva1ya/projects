// Kevalya Khandelwal 590012117
import java.util.Scanner;
public class identitymatrixidentify {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the size of the matrix (n x n): ");
        int n = sc.nextInt();
        int[][] matrix = new int[n][n];
        System.out.println("Enter the matrix elements:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        if (isIdentityMatrix(matrix, n)) {
            System.out.println("The matrix is an Identity Matrix");
        } else {
            System.out.println("The matrix is NOT an Identity Matrix");
        }   
        sc.close();
    }
    public static boolean isIdentityMatrix(int[][] matrix, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((i == j && matrix[i][j] != 1) || (i != j && matrix[i][j] != 0)) {
                    return false;
                }
            }
        }
        return true;
    }
}