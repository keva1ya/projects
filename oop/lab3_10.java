import java.util.Scanner;
public class lab3_10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a email: ");
        String email = sc.nextLine();
        String[] parts = email.split("@");
        String username = parts[0];
        System.out.println("Username: " + username);
    }
}
