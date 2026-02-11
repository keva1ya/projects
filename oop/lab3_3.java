import java.util.Scanner;
public class lab3_3 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("enter a string");
        String s1= sc.next();
        int x= s1.length()-1;
        System.out.println("the starting of the string "+ s1.charAt(0)+" the end of the string "+s1.charAt(x));
    }
}