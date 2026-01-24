public class Students
{
    String name;
    int age;

    void givedetails(String n, int a)
    {
        name = n;
        age = a;
    }

    void show()
    {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static void main(String[] args)
    {
        Students s = new Students();
        s.givedetails("Kevalya", 20);
        s.show();
    }
}
