#include <stdlib.h>
#include <stdio.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x,int y);
} intHeap_T;

int gt(int x, int y);
int lt(int x, int y);
int hs(int *x, int size, int (*compare)(int x, int y));
int store(intHeap_T *heap, int value);
int retrieve(intHeap_T *heap, int *rvalue);

int hs(int *x, int size, int (*compare)(int x, int y)) {
   intHeap_T *heap = (intHeap_T *)malloc(sizeof(intHeap_T));
   int i = 0;
   if (size == 0 || x == NULL || compare == NULL) {
      return -1;
   }
   heap->size = size;
   heap->store = (int *)malloc(sizeof(int)*size);
   heap->end = 0;
   heap->compare = compare;
   for (; i<size; i++) {
      store(heap, x[i]);
   }
   for (i=0; i<size; i++) {
      retrieve(heap, &(x[i]));
   }
   return 0;
}

int store(intHeap_T *heap, int value) {
   int ind = heap->end + 1;
   int par = 0;
   int swp = 0;
   if (heap == NULL || heap->store == NULL) {
      return -1;
   }
   heap->store[heap->end] = value;
   heap->end = heap->end + 1;
   while (ind > 1) {
      par = (int)(ind / 2);
      if ((heap->compare)(heap->store[ind-1], heap->store[par-1]) == 1) {
         swp = heap->store[par-1];
         heap->store[par-1] = heap->store[ind-1];
         heap->store[ind-1] = swp;
         ind = par;
      } else {
         break;
      }
   }
   return 0;
}

int retrieve(intHeap_T *heap, int *rvalue) {
   int ind = 1;
   int sel = 0;
   int end = 1;
   int swp = 0;
   if (heap == NULL || heap->store == NULL || rvalue == NULL || heap->end == 0) {
      return -1;
   }
   while (end*2 <= heap->end) {
      end = end*2;
   }
   end = end - 1;
   if (end == heap->end) { end = (int)((end + 1)/2) - 1; }
   *rvalue = (heap->store)[0];
   heap->end = heap->end - 1;
   heap->store[0] = heap->store[heap->end];
   while (ind*2 < heap->end) {
      if ((heap->compare)(heap->store[ind*2-1], heap->store[ind*2]) == 1) {
         sel = ind*2;
      } else {
         sel = ind*2+1;
      }
      if ((heap->compare)(heap->store[ind-1], heap->store[sel-1]) == 0) {
         swp = heap->store[sel-1];
         heap->store[sel-1] = heap->store[ind-1];
         heap->store[ind-1] = swp;
         ind = sel;
      } else {
         break;
      }
   }
   return 0;
}

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