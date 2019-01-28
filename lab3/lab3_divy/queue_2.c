#include <stdio.h>
#include <stdlib.h>

struct queue {
    int data;
    struct queue *next;
}; 
typedef struct queue queue;

int enqueue(queue **structure, int new_data);
int dequeue(queue **structure, int first);
int peek(queue *structure);

int enqueue(queue **structure, int new_data) {
    if (structure == NULL) {
        return -1;
    }
    else if (*structure == NULL) {
        *structure = (queue *)malloc(sizeof(queue));
        (*structure)->data = new_data;
        (*structure)->next = NULL;
    }
    else {
        enqueue(&((*structure)->next), new_data);
    }
    return 0;
}

int dequeue(queue **structure, int first) {
    queue *old_head;
    if ((structure == NULL) || (*structure == NULL)) {
        return -1;
    }
    else {
        first = (*structure)->data;
        old_head = *structure;
        *structure = &((*structure)->next);
        free(old_head);
        old_head = NULL;
    }
    return 0;
}

int peek(queue *structure) {
    int i = 0;
    printf("[");
    while (structure != NULL) {
        printf("%d,", structure->data);
        structure = structure->next;
    }
    printf("]\n");
    return 0;
}

int main(void) {
    queue *q = NULL;
    int add = 0;
    int i = 0;
    while (scanf("%d", &add) != EOF) {
        enqueue(&q, add);
    }
    peek(q);
    for (i = 0; i < 5; i++) {
        dequeue(&q, add);
        printf("Dequeued: %d\n", add);
    }
    /* peek(q); */
    return 0;
}