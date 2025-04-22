//write a program to implement basic operations of queue using array 
//operations are- enqueue, dequeue, display, peak

#include <stdio.h>
#define SIZE 5  

int queue[SIZE], front = -1, rear = -1;
//enqueue
void enqueue(int value) {
    if (rear == SIZE - 1) {
        printf("overflow\n");
        return;
    }
    if (front == -1) front = 0;
    queue[++rear] = value;
    printf("%d enqueued\n", value);
}
//dequeue
void dequeue() {
    if (front == -1 || front > rear) {
        printf("underflow\n");
        front = rear = -1;
        return;
    }
    printf("%d dequeued\n", queue[front++]);
}
//peek
void peek() {
    if (front == -1 || front > rear)
        printf("empty queue\n");
    else
        printf("Front: %d\n", queue[front]);
}
//display
void display() {
    if (front == -1 || front > rear) {
        printf("empty queue\n");
        return;
    }
    printf("Queue: ");
    for (int i = front; i <= rear; i++)
        printf("%d ", queue[i]);
    printf("\n");
}

int main() {
    int choice, value;
    while (1) {
        printf("\n1. Enqueue\n2. Dequeue\n3. Peek\n4. Display\n5. Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: 
                printf("Enter value: ");
                scanf("%d", &value);
                enqueue(value);
                break;
            case 2: 
            dequeue();
            break;
            case 3: 
            peek();
            break;
            case 4: 
            display();
            break;
            case 5:
            return 0;
            default: printf("enter valid choice\n");
        }
    }
}
