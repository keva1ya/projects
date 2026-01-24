public class explicittypecast {
    public static void main(String[] args) {
        int basesalary=50000;
        double precisebonus=789.99;
        int roundedbonus=(int) precisebonus;
        int totalsalary=basesalary+roundedbonus;
        System.out.println(totalsalary);
        System.out.println(roundedbonus);
    }
    
}
