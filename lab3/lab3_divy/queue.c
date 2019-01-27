#include <stdio.h>
#include <stdlib.h>

struct queue {
   int *store;
   int start;
   int end;
   int length;
   int flipped;  /* -1 = false, 1 = true */
};
typedef struct queue queue;

int init_queue(queue *in, int length);
int enqueue(queue *in, int new_data);
int dequeue(queue *in);

int init_queue(queue *in, int length) {
   if (in == NULL) {
      return -1;
   }
   in->store = (int *)malloc(sizeof(int) * length);
   in->start = 0;
   in->end = 0;
   in->length = length;
   in->flipped = 1;
   return 0;
}

int enqueue(queue *in, int new_data) {
   if (in == NULL) {
      return -1;
   }
   else if (((in->end - in->start) * in->flipped) + 1 >= in->length) {
      return -1;
   }
   if (in->end + 1 == in->length) {
      in->end = 0;
      in->flipped *= -1;
   }
   else {
      in->end += 1;
   }
   (in->store)[in->end] = new_data;
   return 0;
}

int dequeue(queue *in) {
   if (in == NULL) {
      return -1;
   }
   else if (in->end == in->start) {
      return -1;
   }
}