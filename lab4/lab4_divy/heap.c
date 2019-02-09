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
int delHeap(HeapType *pHeap, int *key);
int max(int a, int b);
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

int inorder(HeapType *pHeap, int **output, int *o_size) {  /* LNR */
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
   int i = 0;
   if (pHeap == NULL) {
      return -1;
   }
   for (i = 0; i < pHeap->size; i++) {
      if (key == (pHeap->store)[i]) {
         return 1;
      }
   }
   return 0;
}

int max(int a, int b) {
   if (a > b) {
      return a;
   }
   else {
      return b;
   }
}

int delHeap(HeapType *pHeap, int *key) {
   int index = 0, l = 0, r = 0, swap = 0, cnt = 0;
   if (pHeap == NULL) {
      return -1;
   }
   *key = (pHeap->store)[0];
   if (pHeap->end > 1) {
      (pHeap->store)[0] = (pHeap->store)[pHeap->end - 1];
   }
   else {
      (pHeap->store)[0] = 0;
      return 0; 
   }
   pHeap->end -= 1;
   while (1) {
      if (2*index + 1 < pHeap->end) {
         l = 2*index + 1;
         cnt += 1;
      }
      if (2*index + 2 < pHeap->end) {
         r = 2*index + 2;
         cnt += 2;
      }
      if (cnt == 0) {
         return 0;
      }
      if (cnt == 1) {
         if ((pHeap->store)[index] < (pHeap->store)[l]) {
            swap = (pHeap->store)[index];
            (pHeap->store)[index] = (pHeap->store)[l];
            (pHeap->store)[l] = swap;
            index = l;
         }
         else {
            return 0;
         }
      }
      else if (cnt == 3) {
         if (max((pHeap->store)[l], (pHeap->store)[r]) == (pHeap->store)[l]) {
            swap = (pHeap->store)[index];
            (pHeap->store)[index] = (pHeap->store)[l];
            (pHeap->store)[l] = swap;
            index = l;
         }
         else if (max((pHeap->store)[l], (pHeap->store)[r]) == (pHeap->store)[r]) {
            swap = (pHeap->store)[index];
            (pHeap->store)[index] = (pHeap->store)[r];
            (pHeap->store)[r] = swap;
            index = r;
         }
         else {
            return 0;
         }
      }

      cnt = 0;
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


