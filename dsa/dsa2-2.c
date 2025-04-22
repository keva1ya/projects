#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct college {
    int roll;
    char name[50];
    char department[50];
};

int main() {
    int num_students = 3;
    struct college* students = (struct college*)malloc(num_students * sizeof(struct college));

    students[0].roll = 590012117; strcpy(students[0].name, "Kevalya"); strcpy(students[0].department, "CS");
    students[1].roll = 590016618; strcpy(students[1].name, "Deepanshu"); strcpy(students[1].department, "Mechanical");
    students[2].roll = 590015171; strcpy(students[2].name, "Suryansh"); strcpy(students[2].department, "Civil");

    printf("Original Students:\n");
    for (int i = 0; i < num_students; i++) {
        printf("Roll: %d, Name: %s, Department: %s\n", students[i].roll, students[i].name, students[i].department);
    }

    num_students++;
    students = (struct college*)realloc(students, num_students * sizeof(struct college));

    int position = 1; 
    for (int i = num_students - 1; i > position; i--) {
        students[i] = students[i - 1];
    }

    students[position].roll = 590017525;
    strcpy(students[position].name, "Badri");
    strcpy(students[position].department, "Design");

    printf("\nUpdated Students:\n");
    for (int i = 0; i < num_students; i++) {
        printf("Roll: %d, Name: %s, Department: %s\n", students[i].roll, students[i].name, students[i].department);
    }

    free(students);
    return 0;
}
