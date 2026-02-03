import java.util.Scanner;
public class userinmaxarray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the number of elements: ");
        int n = sc.nextInt();
        int[] array = new int[n];
        System.out.println("enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            System.out.print("element " + (i + 1) + ": ");
            array[i] = sc.nextInt();
        }
        int max = array[0];
        for (int i = 1; i < n; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        System.out.println("the maximum element is: " + max);
    }
}
