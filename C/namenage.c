#include <stdio.h>
int main ()

{
    int age ;
    char name [100];
    printf("Enter your name:");
    scanf ("%s", &name);
    printf("Enter your age: ");
    scanf("%d" , &age);

    printf ("You are %d years old and was named %s by your parents \n", age, name  );
    return 0;
}