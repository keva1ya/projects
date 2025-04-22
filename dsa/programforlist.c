#include <stdio.h>
#include <stdlib.h>

// Node structure
struct node {
    int data;
    struct node* next;
};

// Linked list structure
struct singlylinkedlist {
    struct node* head;
};

// Function to create a linked list
void initializeList(struct singlylinkedlist* list) {
    list->head = NULL;
    printf("Linked list initialized\n");
}

// Function to insert a node at the top
void insertattop(struct singlylinkedlist* list, int data) {
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    if (!newnode) {
        printf("Memory allocation failed\n");
        return;
    }
    newnode->data = data;
    newnode->next = list->head;
    list->head = newnode;
    printf("Inserted %d at the top\n", data);
}

// Function to delete a node from the top
void deleteattop(struct singlylinkedlist* list) {
    if (list->head == NULL) {
        printf("List is empty Nothing to delete\n");
        return;
    }
    struct node* temp = list->head;
    int removeddata = temp->data;
    list->head = list->head->next;
    free(temp);
    printf("Deleted %d from the top\n", removeddata);
}

// Function to traverse and print the linked list
void traverse(struct singlylinkedlist* list) {
    if (list->head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct node* current = list->head;
    printf("Linked List: ");
    while (current) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Menu driven program
int main() {
    struct singlylinkedlist sll;
    int choice, data;
    
    while (1) {
        printf("\nMenu:\n");
        printf("1.Create New List\n");
        printf("2.Insert at top\n");
        printf("3.Delete at top \n");
        printf("4.Traverse the list \n");

        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                 initializeList(&sll);
                break;
            case 2:
            printf("Enter data to insert: ");
                scanf("%d", &data);
                insertattop(&sll, data);
                break;
                
            case 3:
            deleteattop(&sll);
                break;
                
            case 4:
            traverse(&sll);
                break;

            default:
                printf("Invalid choice Please enter a valid option\n");
        }
    }
    return 0;
}
