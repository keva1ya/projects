import java.util.Scanner;

public class simpleint {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter principle");
        float principle = sc.nextFloat();
        System.out.print("enter rate");
        float rate = sc.nextFloat();
        System.out.print("enter time");
        float time = sc.nextFloat();
        float si = (principle * rate * time) / 100;
        System.out.print("Simple Interest: " + si);
    }
}
