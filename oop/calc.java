import java.util.Scanner;

public class calc {
    int add(int a, int b) {
        return a + b;
    }
    
    int sub(int k, int l) {
        return k - l;
    }
    
    int mul(int v, int w) {
        return v * w;
    }
    
    int div(int c, int d) {
        if (d == 0) {
            System.out.println("bruh dont try to divide by 0");
            return 0;
        }
        return c / d;
    }
    
    public static void main(String[] args) {
        calc c = new calc();
        Scanner sc = new Scanner(System.in);{
            System.out.println("select operation 1.add, 2.subtract, 3.multiply, 4.divide");
            int choice = sc.nextInt();
            
            System.out.println("enter first number:");
            int a = sc.nextInt();
            System.out.println("enter second number:");
            int b = sc.nextInt();
            
            int result = 0;
            if (choice == 1) {
                result = c.add(a, b);
            } else if (choice == 2) {
                result = c.sub(a, b);
            } else if (choice == 3) {
                result = c.mul(a, b);
            } else if (choice == 4) {
                result = c.div(a, b);
            } else {
                System.out.println("choose from the given options bruh");
            }
            System.out.println("Result: " + result);
        }
        sc.close();
    }
}
