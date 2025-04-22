#include<stdio.h>
int main ()
{
    float h, w, b ;
    printf ("enter your height (in meters):");
    scanf ("%f", &h );
    printf ("enter your weight (in kgs): ");
    scanf ("%f", &w);
    b = w/ (h*h) ;
    printf ("Your BMI is %.2f \n", b );

    if (b < 15) {        printf("You are classified as Starving.\n");}

else if (b >= 15 && b <= 17.5) {printf("You are classified as Anorexic.\n");}
else if (b > 17.5 && b <= 18.5) {printf("You are classified as Underweight.\n");} 
else if (b > 18.5 && b <= 24.9) {printf("You are classified as Ideal.\n");}
else if (b >= 25 && b <= 29.9) {printf("You are classified as Overweight.\n");} 
else if (b >= 30 && b <= 39.9) {printf("You are classified as Obese.\n");} 
else if (b >= 40) {printf("You are classified as Morbidly Obese.\n");}  

    return 0 ;
}