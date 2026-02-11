import java.util.Scanner;
public class lab3_15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str1 = sc.next();
        System.out.println("Enter another string: ");
        String str2 = sc.next();
         int x= str1.compareTo(str2);
         if(x==0){
            System.out.println("equal strings");
        }
        else if (x>0) {
            System.out.println("greater string is: "+str1);
        }
        else if (x<0) {
            System.out.println("greater string is: "+str2);
        }
    }
}
