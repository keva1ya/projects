class Parent{
    void display(){
        System.out.println("luke i am your father");
    }
        
}
class Child extends Parent{
    void display(){
        super.display();
        System.out.println("luke you are my child");
        }
}
public class classtemp {
    public static void main(String[] args) {
        Parent p=new Parent();
        Child c= new Child();
        c.display();
    }

}