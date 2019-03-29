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
int store(intHeap_T *heap, int value);
int retrieve(intHeap_T *heap, int *rvalue);

int main(void) {
   intHeap_T *heap = (intHeap_T *)malloc(sizeof(intHeap_T));
   heap->size = 1000;
   heap->store = (int *)malloc(sizeof(int) * heap->size);
   heap->end = 0;
   heap->compare = gt;
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