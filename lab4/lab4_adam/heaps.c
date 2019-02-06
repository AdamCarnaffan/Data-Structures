#include <stdlib.h>
#include <stdio.h>


typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

struct queue {
   int val;
   struct queue *next;
};

typedef struct queue queue;


int initHeap(HeapType *,int);
int initOutArray(int, int **, int *);
int inorder(HeapType *, int **, int *);
int preorder(HeapType *, int **, int *);
int postorder(HeapType *, int **, int *);
int addHeap(HeapType *, int);
int shiftValue(HeapType *, int);
int getParentIndex(int);
int getLeftIndex(int);
int getRightIndex(int);

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
   printf("PRE\n");
   if (preorder(root, &pr, &size) == 0) {
      for (c=0; c<size; c++) {
         printf("%d\n", pr[c]);
      }
   }
   printf("IN\n");
   if (inorder(root, &pr, &size) == 0) {
      for (c=0; c<size; c++) {
         printf("%d\n", pr[c]);
      }
   }
   printf("POST\n");
   if (postorder(root, &pr, &size) == 0) {
      for (c=0; c<size; c++) {
         printf("%d\n", pr[c]);
      }
   }
   return 0;
}

int push(queue **root, int val) {
   if (root == NULL) {
      return -1;
   }
   if (*root != NULL) {
      return push(root, val);
   } else {
      *root = (queue *)malloc(sizeof(queue));
      (*root)->val = val;
      (*root)->next = NULL;
   }
}

int pop(queue **root, int *ret) {
   if (root == NULL) {
      return -1;
   } else if (*root == NULL) {
      *ret = 0;
      return -1;
   }
   *ret = (*root)->val;
   *root = (*root)->next;
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
   int c, current = 1;
   int l, r, temp = -1;
   int from = -1; /* -1 for left, 0 for parent, 1 for right */
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   while (current < pHeap->end) {
      current = getLeftIndex(current);
   }
   current = getParentIndex(current);
   for (c=0; c<pHeap->end; c++) {
      if (temp = getLeftIndex(current) < pHeap->end && from != -1) {
         current = temp;
         from = -1;
      } else if (temp = getRightIndex(current) < pHeap->end && from == 0) {
         current = temp;
         from = 1;
      } else if (from != 1) {
         current = getParentIndex(current);
         from = 0;
      } else {
         current = getParentIndex(getParentIndex(current));
         from = 0;
      }
      (*output)[c] = (pHeap->store)[current-1];
   }
   return 0;
}

int postorder(HeapType *pHeap, int **output, int *o_size) {
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
   int c = 0;
   int *st = pHeap->store;
   if (pHeap == NULL) { return -1; }
   if (pHeap->end >= pHeap->size - 1) {  
      return -1;
   }
   // for (c=0; c<pHeap->end; c++) {
   //    if ((pHeap->store)[c] == key) {
   //       return -1;
   //    }
   // }
   pHeap->end = pHeap->end + 1;
   st[(pHeap->end)] = key;
   return shiftValue(pHeap, pHeap->end);
}