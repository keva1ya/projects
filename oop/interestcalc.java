public class interestcalc {
    public static void main(String[] args) {
        double principal=17000;
        double roi=0.05;
        double time=1;
        double interest= principal*roi*time;
        double amount= principal+interest;
        System.out.println("The interest after " + time + "year(s) " + "at " + roi +"% interest is-" + interest);
        System.out.println("The total amount is- " + amount); }
    
}

