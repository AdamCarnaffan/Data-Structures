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
   int i = 0, depth = 0;
   if ((pHeap == NULL) || (pHeap->end == pHeap->size)) {
      return -1;
   }
   (pHeap->store)[pHeap->end] = key;
   pHeap->end += 1;
   i = pHeap->end - 1;
   depth = i/2;
   printf("CHILD IS : %d, PARENT IS : %d, DEPTH IS: %d, i is: %d\n", (pHeap->store)[i], (pHeap->store)[i - depth], depth, i);
   while ((pHeap->store)[i] > (pHeap->store)[i - depth]) {
      (pHeap->store)[i], (pHeap->store)[i - depth] = (pHeap->store)[i - depth], (pHeap->store)[i];
      i -= depth;
   }
   disp_Heap(pHeap);
   return 0;
}

int disp_Heap(HeapType *pHeap) {
   int i = 0;
   printf("[");
   for (i = 0; i < pHeap->end; i++) {
      printf("%d ", (pHeap->store)[i]);
   }
   printf("]\n");
}

int disp_array(int *array, int size) {
   int i = 0;
   printf("[");
   for (i = 0; i < size; i++) {
      printf("%d ", array[i]);
   }
   printf("]\n");
   return 0;
}

int main(void) {
   HeapType *pHeap = (HeapType *)malloc(sizeof(HeapType));
   int size = 0, o_size = 0, *output;
   printf("Input Size:\n");
   scanf("%d", &size);
   initHeap(pHeap, size);
   addHeap(pHeap, 10);
   addHeap(pHeap, 20);
   addHeap(pHeap, 30);
   addHeap(pHeap, 12);
   addHeap(pHeap, 4);
   addHeap(pHeap, 7);
   addHeap(pHeap, 18);
   addHeap(pHeap, 19);
   addHeap(pHeap, 100);
   //inorder(pHeap, &output, &o_size);
   //disp_Heap(pHeap);
   //disp_array(output, size);
   return 0;
}