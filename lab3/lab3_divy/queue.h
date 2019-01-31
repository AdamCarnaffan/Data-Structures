struct queue {
    int data;
    struct queue *next;
}; 
typedef struct queue queue;

int enqueue(queue **structure, int new_data);
int dequeue(queue **structure, int *first);
int peek(queue *structure);
int len_queue(queue *structure);