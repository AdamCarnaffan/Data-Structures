#include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x, int y);
} intHeap_T;

int lt(int x, int y);
int gt(int x, int y);
int store(intHeap_T* heap, int value);
int retrieve(intHeap_T* heap, int *rvalue);

int lt(int x, int y) {
   if (x < y) {
      return 1;
   }
   return 0;
}

int gt(int x, int y) {
   if (x > y) {
      return 1;
   }
   return 0;
}

int store(intHeap_T *heap, int value) {
   if ((heap == NULL) || (heap->end == heap->size)) {
      return -1;
   }
   int n = heap->end, parent = 0, swapper = 0;
   (heap->store)[n] = value;
   heap->end += 1;
   while (n > 0) {
      parent = (n - 1)/2;
      if (heap->compare((heap->store)[parent], (heap->store)[n]) == 1) {
         swapper = (heap->store)[n];
         (heap->store)[n] = (heap->store)[parent];
         (heap->store)[parent] = swapper;
      }
      else { break; }
      n = parent;
   }
   return 0;
}

int retrieve(intHeap_T* heap, int *rvalue) {
   if ((heap == NULL) || (heap->end <= 0)) {
      return -1;
   }
   *rvalue = (heap->store)[0];
   heap->end -= 1;
   (heap->store)[0] = (heap->store)[heap->end];
   if (heap->end == 0) {
      return 0;
   }
   int parent = 0, swap = 0, child = 0;
   while (1) {
      swap = parent;
      child = 2*parent + 1;
      if (child >= heap->end) { break; }
      else if (heap->compare((heap->store)[parent], (heap->store)[child]) == 1) { swap = child; }
      if ((child + 1 < heap->end) && (heap->compare((heap->store)[swap], (heap->store)[child + 1]) == 1)) { swap = child + 1; }
      if (swap == parent) { break; }
      else {
         child = (heap->store)[swap];
         (heap->store)[swap] = (heap->store)[parent];
         (heap->store)[parent] = child;
         parent = swap;
      }
   }
   return 0;
}
