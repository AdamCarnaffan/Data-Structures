#include <stdlib.h>
#include <stdio.h>
#include "heap.h"

int main(void) {
   int *pr = NULL;
   int size,c = 0;
   HeapType *root = (HeapType *)malloc(sizeof(HeapType));
   initHeap(root, 45);
   for (c=0; c<45; c++) {
      addHeap(root, c);
      printf("ADDED %d\n", c);
   }
   printf("PRE\n=-=-=-=-=-=\n");
   if (preorder(root, &pr, &size) == 0) {
      for (c=0; c<size; c++) {
         printf("%d\n", pr[c]);
      }
   }
   printf("IN\n=-=-=-=-=-=\n");
   if (inorder(root, &pr, &size) == 0) {
      for (c=0; c<size; c++) {
         printf("%d\n", pr[c]);
      }
   }
   printf("POST\n=-=-=-=-=-=\n");
   if (postorder(root, &pr, &size) == 0) {
      for (c=0; c<size; c++) {
         printf("%d\n", pr[c]);
      }
   }
   delHeap(root, &c);
   printf("Removed: %d\n", c);
   return 0;
}