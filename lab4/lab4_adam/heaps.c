#include <stdlib.h>
#include <stdio.h>


typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;


int initHeap(HeapType *,int);
int inorder(HeapType *, int **, int *);
int preorder(HeapType *, int **, int *);
int postorder(HeapType *, int **, int *);
int addHeap(HeapType *, int);
int shiftValue(HeapType *, int);
int getParentIndex(int);
int initOutArray(int, int **, int *);

int main(void) {
   int *pr = NULL;
   int size,c = 0;
   HeapType *root = (HeapType *)malloc(sizeof(HeapType));
   initHeap(root, 50);
   addHeap(root, 10);
   addHeap(root, 25);
   addHeap(root, 55);
   addHeap(root, 70);
   addHeap(root, 8);
   if (inorder(root, &pr, &size) == 0) {
      for (c=0; c<size; c++) {
         printf("%d\n", pr[c]);
      }
   }
   return 0;
}

int initHeap(HeapType *pHeap, int size) {
   if (pHeap == NULL) { return -1; }
   pHeap->size = size;
   pHeap->end = 0;
   pHeap->store = (int *)malloc(sizeof(int)*size);
   if (pHeap->store == NULL) {
      return -1;
   }
   return 0;
}

int inorder(HeapType *pHeap, int **output, int *o_size) {
   int c = 0;
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   
   return 0;
}

int initOutArray(int size, int **out, int *o_size) {
   int c = 0;
   if (out == NULL || o_size == NULL) { return -1; }
   *out = (int *)malloc(sizeof(int)*size);
   *o_size = size;
   return 0;
}

int preorder(HeapType *pHeap, int **output, int *o_size) {
   int c = 0;
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   for (c=0; c<pHeap->end; c++) {
      (*output)[c] = (pHeap->store)[c];
   }
   return 0;
}

int getParentIndex(int index) {
   if (index == 0) { return -1; }
   return (int)(index / 2);
}

int getLeftIndex(int index) {
   return index*2;
}

int getRightIndex(int index) {
   return index*2 + 1;
}

int shiftValue(HeapType *pHeap, int ind) {
   int parentInd = 0;
   int temp;
   if (pHeap == NULL) { return -1; }
   if (ind == 0) {
      return 0;
   }
   parentInd = getParentIndex(ind);
   if ((pHeap->store)[parentInd] < (pHeap->store)[ind]) {
      temp = (pHeap->store)[parentInd];
      (pHeap->store)[parentInd] = (pHeap->store)[ind];
      (pHeap->store)[ind] = temp;
      return shiftValue(pHeap, parentInd);
   } else {
      return 0;
   }
}

int addHeap(HeapType *pHeap, int key) {
   int *st = pHeap->store;
   if (pHeap == NULL) { return -1; }
   if (pHeap->end >= pHeap->size - 1) {  
      return -1;
   }
   pHeap->end = pHeap->end + 1;
   st[(pHeap->end)] = key;
   return shiftValue(pHeap, pHeap->end);
}