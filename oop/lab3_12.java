import java.util.Scanner;
public class lab3_12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        String[] words=str.split(" ");
        System.out.println("total words: "+words.length);
    }
}
