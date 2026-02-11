import java.util.Scanner;
public class lab3_11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        String s1=str.replace(" ", "-");
        System.out.println(s1);
    }   
}
