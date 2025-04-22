#include <stdio.h>
#include <stdlib.h>

#define MAX 5 

int stack[MAX], top = -1;
void createStack() {
    top = -1;
    printf("Stack created.\n");
}
void push() {
    int value;
    if (top == MAX - 1) {
        printf("overflow\n");
        return;
    }
    printf("Enter value to push: ");
    scanf("%d", &value);
    stack[++top] = value;
    printf("%d pushed into the stack.\n", value);
}
void pop() {
    if (top == -1) {
        printf("underflow\n");
        return;
    }
    printf("%d popped from the stack.\n", stack[top--]);
}
void peek() {
    if (top == -1) {
        printf("Stack empty\n");
        return;
    }
    printf("Top element is: %d\n", stack[top]);
}
void display() {
    if (top == -1) {
        printf("Stack empty.\n");
        return;
    }
    printf("elements: ");
    for (int i = top; i >= 0; i--) {
        printf("%d ", stack[i]);
    }
}
int main() {
    int choice;
    while (1) {
        printf("\nStack Operations:\n");
        printf("1) Create Stack\n");
        printf("2) Push\n");
        printf("3) Pop\n");
        printf("4) Peek\n");
        printf("5) Display\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                createStack();
                break;
            case 2:
                push();
                break;
            case 3:
                pop();
                break;
            case 4:
                peek();
                break;
            case 5:
                display();
                break;
            default:
                printf("invalid choice, enter another \n");
        }
    }
  return 0;
}