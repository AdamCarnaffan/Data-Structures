#include <stdio.h>
#include <stdlib.h>

typedef struct queue {
    int *store;
    int len;
    int end;
} queue;

int initizialize(queue **structure, int size);
int enqueue(queue *structure, int new_data);
int dequeue(queue *structure);
int display(queue *structure);

int initizialize(queue **structure, int size) {
   int i = 0;
   if (structure == NULL) {
      return -1;
   }
   *structure = (queue *)malloc(sizeof(queue));
   (*structure)->store = (int *)malloc(sizeof(int) * size);
   (*structure)->len = size;
   (*structure)->end = 0;
    return 0;
}

int enqueue(queue *structure, int new_data) {
    int i = 0;
    if ((structure == NULL) || (structure->end == structure->len)) {
        return -1;
    }
    for (i = (structure->end); i > 0; i = i - 1) {
        (structure->store)[i] = (structure->store)[i - 1];
    }
    (structure->store)[0] = new_data;
    structure->end += 1;
    return 0;
}

int dequeue(queue *structure) {
    if ((structure == NULL) || (structure->end == 0)) {
        return -1;
    }
    structure->end -= 1;
    return (structure->store)[structure->end];
}

int display(queue *structure) {
    int i = 0;
    if (structure == NULL) {
        return -1;
    }
    printf("[");
    for (i = 0; i < structure->end; i++) {
        printf("%d,", (structure->store)[i]);
    }
    printf("]\n");
    return 0;
}

int main(void) {
    queue *structure = NULL;
    int i = 0;
    int size = 0;
    printf("Size of Queue:\n");
    scanf("%d", &size);
    initizialize(&structure, size);
    for (i = 0; i < size; i++) {
        enqueue(structure, i + 1);
    }
    display(structure);
    for (i = 0; i < size/2; i++) {
        printf("Dequeued: %d\n", dequeue(structure));
    }
    display(structure);
    for (i = 0; i < size; i++) {
        enqueue(structure, i + 1);
    }
    display(structure);
    return 0;
}