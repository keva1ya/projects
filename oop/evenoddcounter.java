import java.util.Scanner;
public class evenoddcounter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            System.out.print("element " + (i + 1) + ": ");
            arr[i] = sc.nextInt();
        }
        int ecount=0;
        int ocount=0;
        for (int i = 0; i < n; i++) {
            if (arr[i] % 2 == 0) {
                ecount++;
            }
            else if (arr[i] % 2==1) 
            {
                ocount++;
            }
        }
        System.out.println("count of even numbers=" +ecount);
        System.out.println("count of odd numbers="+ocount);
    }    
}
