import java.util.Scanner;

public class sumuserin {
    public void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.print("enter a number: ");
        int num1=sc.nextInt();
        System.out.print("enter another number: ");
        int num2=sc.nextInt();
        int sum=num1+num2; 
        System.out.println("the sum of " + num1 + " and " + num2 + " is- " + sum);
    }
}
