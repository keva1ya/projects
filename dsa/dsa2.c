#include <stdio.h>
struct college {
    int roll;
    char name[50];
    char department[50];
};

int main() {
    struct college students[3] = {
        {590012117, "Kevalya", "cs"},
        {590016618, "Deepanshu", "civil"},
        {590015178, "Suryansh", "mechanical"}
    };

 
    printf("Details of Students:\n");
    for (int i = 0; i < 3; i++) {
        printf("Roll: %d, Name: %s, Department: %s\n", students[i].roll, students[i].name, students[i].department);
    }

    return 0;
}
