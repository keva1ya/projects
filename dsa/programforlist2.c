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

// Function to free memory of the existing list
void freeList(struct singlylinkedlist* list) {
    struct node* current = list->head;
    struct node* temp;
    while (current != NULL) {
        temp = current;
        current = current->next;
        free(temp);
    }
    list->head = NULL;
}

// Function to initialize (or reset) a linked list
void initializeList(struct singlylinkedlist* list) {
    freeList(list);  // Ensure no memory leaks
    list->head = NULL;
    printf("Linked list initialized\n");
}

// Function to insert a node at the top
void insertAtTop(struct singlylinkedlist* list, int data) {
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

// Function to insert at any position k
void insertatposition(struct singlylinkedlist* list, int data, int position) {
    if (position <= 1) {
        insertAtTop(list, data);
        return;
    }

    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    if (!newnode) {
        printf("Memory allocation failed\n");
        return;
    }
    newnode->data = data;
    newnode->next = NULL;

    struct node* current = list->head;
    struct node* prev = NULL;
    int count = 1;

    while (current != NULL && count < position) {
        prev = current;
        current = current->next;
        count++;
    }

    if (prev == NULL) {
        list->head = newnode;
    } else {
        prev->next = newnode;
    }
    newnode->next = current;
    printf("Inserted %d at position %d\n", data, position);
}

// Function to delete a node from the top
void deleteAtTop(struct singlylinkedlist* list) {
    if (list->head == NULL) {
        printf("List is empty. Nothing to delete.\n");
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
    struct singlylinkedlist x;
    int choice, data, position;
    
    while (1) {
        printf("\nMenu:\n");
        printf("1. Create New List\n");
        printf("2. Insert at top\n");
        printf("3. Delete at top\n");
        printf("4. Traverse the list\n");
        printf("5. Insert at position k\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                initializeList(&x);
                break;
            case 2:
                printf("Enter data to insert: ");
                scanf("%d", &data);
                insertAtTop(&x, data);
                break;
            case 3:
                deleteAtTop(&x);
                break;
            case 4:
                traverse(&x);
                break;
            case 5:
                printf("Enter data to insert: ");
                scanf("%d", &data);
                printf("Enter position: ");
                scanf("%d", &position);
                insertatposition(&x, data, position);
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    }
    return 0;
}
