import java.util.Scanner;
public class lab3_8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        int count = 0;
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < str.length(); i++) {
            if (vowels.contains(str.substring(i, i + 1))) {
                count++;
            }
        }
        System.out.println("total vowels: " + count);
    }
}