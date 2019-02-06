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
int disp_Heap(HeapType *pHeap);
int disp_array(int *array, int size);
int exponential(int base, int power);
int get_depth(int pair);

int initHeap(HeapType *pHeap, int size) {
   if (pHeap == NULL) {
      return -1;
   }
   pHeap->store = (int *)malloc(sizeof(size));
   if (pHeap->store == NULL) {
      return -1;
   }
   pHeap->size = size;
   pHeap->end = 0;
   return 0;
}

int inorder(HeapType *pHeap, int **output, int *o_size) {
   int i = 0;
   if (pHeap == NULL) {
      return -1;
   }
   *o_size = pHeap->end - 1;
   *output = (int *)malloc(sizeof(int) * (*o_size));
   if (*output == NULL){
      return -1;
   }
   i = pHeap->end;
   while (i  >= 0) {
      if (i % 2*i == 0) {
         (*output)[i] = (pHeap->store)[(pHeap->end)/2*1];
      }
      else if (i % (2*i + 1) == 0) {
         (*output)[i] = (pHeap->store)[(pHeap->end)/(2*i + 1)];
      }
      else if (i % (2*i + 2) == 0) {
         (*output)[i] = (pHeap->store)[(pHeap->end)/(2*i + 2)];
      }
      i -= 1;
   }
   return 0;
}

int addHeap(HeapType *pHeap, int key) {
   int i = 0, depth = 0, swap = 0, jump = 0;
   if ((pHeap == NULL) || (pHeap->end == pHeap->size)) {
      return -1;
   }
   (pHeap->store)[pHeap->end] = key;
   i = pHeap->end;
   pHeap->end += 1;
   if (i == 1) {
      return 0;
   }
   depth = get_depth((i + 1)/2);
   jump = exponential(2, depth);
   while ((pHeap->store)[i] > (pHeap->store)[i - jump]) {
      swap = (pHeap->store)[i];
      (pHeap->store)[i] = (pHeap->store)[i - jump];
      (pHeap->store)[i - jump] = swap;
      depth -= 1;
      i -= jump;
      jump = exponential(2, get_depth((i + 1)/2));
   }
   disp_Heap(pHeap);
   return 0;
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

int exponential(int base, int power) {
   int i = 0, answer = 1;
   for (i = 0; i < power; i++) {
      answer *= base;
   }
   return answer;
}

int get_depth(int pair) {
   int depth = 0, i = 0;
   while (exponential(2, depth) <= pair) {
      depth += 1;
   }
   return depth;
}

int main(void) {
   HeapType *pHeap = (HeapType *)malloc(sizeof(HeapType));
   int size = 0, o_size = 0, *output, i = 0;
   printf("Input Size:\n");
   scanf("%d", &size);
   initHeap(pHeap, size);
   for (i = 0; i < 16; i++) {
      addHeap(pHeap, i);
   }
   //inorder(pHeap, &output, &o_size);
   //disp_Heap(pHeap);
   //disp_array(output, size);
   return 0;
}