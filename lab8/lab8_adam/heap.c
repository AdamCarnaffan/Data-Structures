#include <stdlib.h>
#include <stdio.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x, int y);
} intHeap_T;

int gt(int, int);
int lt(int, int);
int store(intHeap_T *, int);
int retrieve(intHeap_T *, int *);

int main(void) {
   intHeap_T *heap;
   heap->store = (int *)malloc(sizeof(int) * 1000);
   heap->size = 1000;
   heap->end = 0;
   heap->compare = lt;
   int i = 0, rvalue = 0;
   for (i = 0; i < 15; i++) {
      store(heap, i);
   }
   for (i = 0; i < heap->end; i++) {
      printf("store[%d] = %d\n", i, (heap->store)[i]);
   }
   printf("\n");
   for (i = 0; i < 5; i++) {
      retrieve(heap, &rvalue);
      printf("rvalue: %d\n", rvalue);
   }
   printf("\n");
   for (i = 0; i < heap->end; i++) {
      printf("store[%d] = %d\n", i, (heap->store)[i]);
   }   
   return 0;
}

int store(intHeap_T *heap, int value) {

}


int retrieve(intHeap_T *heap, int *rvalue) {
   int ind = 0;
   if (heap == NULL || rvalue == NULL || heap->end == 0) {
      return -1;
   }
   *rvalue = heap->store[0];
   heap->end = heap->end - 1;
   heap->store[0] = heap->store[heap->end];
   while (ind <= heap->end) {
      if ()
   }
   
}

int lt(int x, int y) {
   if (x > y) {
      return 0;
   }
   return 1;
}

int gt(int x, int y) {
   if (x < y) {
      return 0;
   }
   return 1;
}