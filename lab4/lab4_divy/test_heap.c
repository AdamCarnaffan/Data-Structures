#include <stdio.h>
#include <stdlib.h>
#include "heap.h"

int main(void) {
   HeapType *pHeap = (HeapType *)malloc(sizeof(HeapType));
   int size = 0, o_size = 0, *output, i = 0, key = 0;
   printf("Input Size:\n");
   scanf("%d", &size);
   initHeap(pHeap, size);
   for (i = 0; i < size; i++) {
      addHeap(pHeap, i);
   }
   printf("Heap: "), disp_Heap(pHeap);
   delHeap(pHeap, &key);
   printf("Heap: "), disp_Heap(pHeap);
   //printf("Output: "), disp_array(output, size);
   printf("Key is: %d", key);
   return 0;
}