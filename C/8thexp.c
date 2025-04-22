#include <stdio.h>

struct Book
{
    int book_id;
    char title[100], author[100], publisher[100], date_of_issue[20], date_of_return[20];
    float price;
    int year_of_publication;
};

void printBookDetails(struct Book book)
{
    printf("\nBook ID: %d\n", book.book_id);
    printf("Title: %s\n", book.title);
    printf("Author: %s\n", book.author);
    printf("Price: %.2f\n", book.price);
    printf("Year of Publication: %d\n", book.year_of_publication);
    printf("Publisher: %s\n", book.publisher);
    printf("Date of Issue: %s\n", book.date_of_issue);
    printf("Date of Return: %s\n", book.date_of_return);
}

int main()
{
    struct Book myBook;

    printf("Enter book ID: ");
    scanf("%d", &myBook.book_id);

    printf("Enter book title (single word): ");
    scanf("%s", myBook.title);

    printf("Enter author name (single word): ");
    scanf("%s", myBook.author);

    printf("Enter price: ");
    scanf("%f", &myBook.price);

    printf("Enter year of publication: ");
    scanf("%d", &myBook.year_of_publication);

    printf("Enter publisher name (single word): ");
    scanf("%s", myBook.publisher);

    printf("Enter date of issue (YYYY-MM-DD): ");
    scanf("%s", myBook.date_of_issue);

    printf("Enter date of return (YYYY-MM-DD): ");
    scanf("%s", myBook.date_of_return);
    printBookDetails(myBook);

    return 0;
}