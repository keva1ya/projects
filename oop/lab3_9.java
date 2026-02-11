import java.util.Scanner;

public class lab3_9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        String clean = str.replaceAll(" ", "").toLowerCase();
        String reversed = "";
        for (int i = clean.length() - 1; i >= 0; i--) {
            reversed += clean.charAt(i);
        }
        if (clean.equals(reversed)) {
            System.out.println("Palindrome");
        } else {
            System.out.println("Not a palindrome");
        }
        sc.close();
    }
}

