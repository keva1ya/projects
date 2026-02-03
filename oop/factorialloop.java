import java.util.Scanner;
public class factorialloop {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("enter a number to find factorial-");
        int factorial=1;
        int num=sc.nextInt();
        for(int i=1;i<=num;i++){
            factorial=factorial*i;
        }
        System.out.println(factorial);
    }
    
}
