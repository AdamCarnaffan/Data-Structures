#include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

int initHeap(HeapType *pHeap, int size);
int inorder(HeapType *pHeap, int **output, int *o_size);
int preorder(HeapType *pHeap, int **output, int *o_size);
int postorder(HeapType *pHeap, int **output, int *o_size);
int addHeap(HeapType *pHeap, int key);
int findHeap(HeapType *pHeap, int key);
int disp_Heap(HeapType *pHeap);
int disp_array(int *array, int size);

int initHeap(HeapType *pHeap, int size) {
   if (pHeap == NULL) {
      return -1;
   }
   pHeap->store = (int *)malloc(sizeof(int) * size);
   if (pHeap->store == NULL) {
      return -1;
   }
   pHeap->size = size;
   pHeap->end = 0;
   return 0;
}

int inorder(HeapType *pHeap, int **output, int *o_size) {  /* NLR */
   int index = 0, node = 0, counter = 0, side = 1, depth = 1; /* left = 1, right = 2 */
   if (pHeap == NULL) {
      return -1;
   }
   *o_size = pHeap->end;
   *output = (int *)malloc(sizeof(int) * (*o_size));
   if (*output == NULL) {
      return -1;
   }
   while (counter < *o_size) {
      if (node == 1) {
         while (index % 2 == 0) {
            index = (index - side)/2;
         }
         index = (index - 1)/2;
         (*output)[counter] = (pHeap->store)[index];
         node = 0;
         side = 2;
         counter += 1;
         continue;
      }
      while (2*index + side < *o_size) {
         index = 2*index + side;
         if (side % 2 == 0) {
            if (2*index + 1 >= *o_size) { node = 1; }
            else { 
               side = 1;
               continue;
            }
            break;
         }
      }
      (*output)[counter] = (pHeap->store)[index];
      counter += 1;
      if (side == 1) { node = 1; }
   }
   return 0;
}

int preorder(HeapType *pHeap, int **output, int *o_size) {  /*NLR*/
   int index = 0, side = 1, counter = 0, node = 1;
   if (pHeap == NULL) {
      return -1;
   }
   *o_size = pHeap->end;
   *output = (int *)malloc(sizeof(int) * (*o_size));
   if (*output == NULL) {
      return -1;
   }
   while (counter < *o_size) {
      if (node == 1) {
         if (side == 1) {
            (*output)[counter] = (pHeap->store)[index];
            counter += 1;
         }
         else {
            while (index % 2 == 0) {
               index = (index - side)/2;
            }
            index = (index - 1)/2;
         }
         node = 0;
         continue;
      }
      while (2*index + side < *o_size) {
         index = 2*index + side;
         (*output)[counter] = (pHeap->store)[index];
         counter += 1;
         if (side % 2 == 0) {
            if (2*index + 1 >= *o_size) {
               break;
            }
            else {
               side = 1;
            }
         }
      }
      node = 1;
      if (side == 1) { side = 2; }
   }
   return 0;
}

int postorder(HeapType *pHeap, int **output, int *o_size) {  /* LRN */
   int index = 0, side = 1, counter = 0, node = 0;
   if (pHeap == NULL) {
      return -1;
   }
   *o_size = pHeap->end;
   *output = (int *)malloc(sizeof(int) * (*o_size));
   if (*output == NULL) {
      return -1;
   } 
   while (counter < *o_size) {
      if (node == 1) {
         while (index % 2 == 0) {
            index = (index - side)/2;
            (*output)[counter] = (pHeap->store)[index];
            counter += 1;
         }
         index = (index - 1)/2;
         side = 2;
         node = 0;
         continue;
      }
      while (2*index + side < *o_size) {
         index = 2*index + side;
         if (side % 2 == 0) {
            if (2*index + 1 >= *o_size) {
               break;
            }
            else {
               side = 1;
            }
         }
      }
      (*output)[counter] = (pHeap->store)[index];
      counter += 1;
      node = 1;
   }
   return 0;
}

int addHeap(HeapType *pHeap, int key) {
   int index = 0, swap = 0, parent = 0;
   if ((pHeap == NULL) || (pHeap->end == pHeap->size)) {
      return -1;
   }
   (pHeap->store)[pHeap->end] = key;
   index = pHeap->end;
   pHeap->end += 1;
   if (index == 0) {
      return 0;
   }
   parent = (index + 1)/2 - 1;
   while ((pHeap->store)[index] > (pHeap->store)[parent]) {
      swap = (pHeap->store)[index];
      (pHeap->store)[index] = (pHeap->store)[parent];
      (pHeap->store)[parent] = swap;
      index = parent;
      parent = (index + 1)/2 - 1;
   }
   return 0;
}

int findHeap(HeapType *pHeap, int key) {
   int index = 0, c1 = 0, c2 = 0, side = 1, node = 0;
   if (pHeap == NULL) {
      return -1;
   }
   while (1) {
      if (node == 1) {
         continue;
      }
      while ((2*index + side < pHeap->end) && ( key > (pHeap->store)[2*index + side])) {
         index = 2*index + side;
      }
      if (key == )
   }
}

int disp_Heap(HeapType *pHeap) {
   int i = 0;
   printf("[");
   for (i = 0; i < pHeap->end; i++) {
      if (i == pHeap->end - 1) {
         printf("%d", (pHeap->store)[i]);
         continue;
      }
      printf("%d,", (pHeap->store)[i]);
   }
   printf("]\n");
}

int disp_array(int *array, int size) {
   int i = 0;
   printf("[");
   for (i = 0; i < size; i++) {
      if (i == size - 1) {
         printf("%d", array[i]);
         continue;
      }
      printf("%d,", array[i]);
   }
   printf("]\n");
   return 0;
}


int main(void) {
   HeapType *pHeap = (HeapType *)malloc(sizeof(HeapType));
   int size = 0, o_size = 0, *output, i = 0;
   printf("Input Size:\n");
   scanf("%d", &size);
   initHeap(pHeap, size);
   for (i = 0; i < size; i++) {
      addHeap(pHeap, i);
   }
   preorder(pHeap, &output, &o_size);
   printf("Heap: "), disp_Heap(pHeap);
   printf("Output: "), disp_array(output, size);
   return 0;
}