import java.util.Scanner;

public class lab3_13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter a sentence: ");
        String sentence = sc.nextLine();
        
        String[] words = sentence.split(" ");
        String result = "";
        
        for (String word : words) {
            for (int i = word.length() - 1; i >= 0; i--) {
                result += word.charAt(i);
            }
            result += " ";
        }
        
        System.out.println("Reversed words: " + result.trim());
        sc.close();
    }
}
