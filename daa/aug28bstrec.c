#include <stdio.h>
#include <stdlib.h>
#include <time.h>
const size_t CAPACITY = 1024;
typedef struct {
    int nodes[1024];
    unsigned char used[1024];
} bst;
size_t lindex(size_t i) { return 2 * i + 1; }
size_t rtindex(size_t i) { return 2 * i + 2; }
int insert(bst *t, int value, size_t idx) {
    if (idx >= CAPACITY) return 0;
    if (!t->used[idx]) {
        t->nodes[idx] = value;
        t->used[idx] = 1;
        return 1;
    }
    if (value < t->nodes[idx])
        return insert(t, value, lindex(idx));
    else
        return insert(t, value, rtindex(idx));
}
int search(const bst *t, int value, size_t idx) {
    if (idx >= CAPACITY || !t->used[idx]) return 0;
    if (value == t->nodes[idx]) return 1;
    if (value < t->nodes[idx])
        return search(t, value, lindex(idx));
    else
        return search(t, value, rtindex(idx));
}
void inorder(const bst *t, size_t idx) {
    if (idx >= CAPACITY || !t->used[idx]) return;
    inorder(t, lindex(idx));
    printf("%d ", t->nodes[idx]);
    inorder(t, rtindex(idx));
}
int main(void) {
    bst tree = {0};
    srand((unsigned)time(NULL));
    size_t n;
    printf("enter number of nodes to insert (default 10): ");
    if (scanf("%zu", &n) != 1 || n == 0) n = 10;
    int range;
    printf("enter max random value (default 100): ");
    if (scanf("%d", &range) != 1 || range <= 0) range = 100;
    for (size_t i = 0; i < n; ++i) {
        int val = rand() % range;
        insert(&tree, val, 0);
    }
    printf("sorted (inorder): ");
    inorder(&tree, 0);
    printf("\n");
    int q;
    printf("enter number to search for: ");
    if (scanf("%d", &q) == 1) {
        if (search(&tree, q, 0))
            printf("found\n");
        else
            printf("not found\n");
    }
    return 0;
}
