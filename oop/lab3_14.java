import java.util.Scanner;
public class lab3_14 {
    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        String vowels = "0123456789";
        boolean hasDigit = true;
        for (int i = 0; i < str.length(); i++) {
            if (!vowels.contains(str.substring(i, i + 1))) {
                hasDigit = false;
            }
        }
        System.out.println("only digits--" + hasDigit);
    }
}
