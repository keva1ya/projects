import java.util.Scanner;
public class mtx3diagonalsum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] matrix = new int[3][3];
        System.out.println("Enter the 3x3 matrix elements:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print("Element [" + i + "][" + j + "]: ");
                matrix[i][j] = sc.nextInt();
            }
        }
        int diagonalsum = 0;
        for (int i = 0; i < 3; i++) {
            diagonalsum += matrix[i][i];
        }
        System.out.println("sum of diagonal elements: " + diagonalsum);
    }
}
