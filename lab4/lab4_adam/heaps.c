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
int findHeap(HeapType *, int);
int delHeap(HeapType *, int *);
int addHeap(HeapType *, int);
int shiftValue(HeapType *, int);
int getParentIndex(int);
int getLeftIndex(int);
int getRightIndex(int);
int print(int);
int expp(int, int);
int moveLargestUp(HeapType *, int);

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

int main(void) {
   int *pr = NULL;
   int size,c = 0;
   HeapType *root = (HeapType *)malloc(sizeof(HeapType));
   initHeap(root, 15);
   for (c=0; c<15; c++) {
      addHeap(root, c);
      printf("ADDED %d\n", c);
      disp_Heap(root);
   }
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
   delHeap(root, &c);
   printf("Removed: %d\n", c);
   disp_Heap(root);
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

int preorder(HeapType *pHeap, int **output, int *o_size) { /* NLR */
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   
   return 0;
}

int inorder(HeapType *pHeap, int **output, int *o_size) {
   int c = 1, x = 0, val = 0, distance = 0;
   int depth = 0,dp = 0;
   int dTrial = 1;
   int ind = 0;
   int step = 1;
   int btmovr = 0;
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   while (c*2 <= pHeap->end) {
      c *= 2;
      depth++;
   }
   dp = expp(2, depth);
   for (c=0; c < pHeap->end; c++) {
      val = c + distance;
      if (btmovr == 1) { distance++; }
      x = 0;
      step = expp(2, x+1);
      dTrial = expp(2, x) - 1;
      while (val % step != dTrial) {
         x++;
         step = expp(2, x+1);
         dTrial = expp(2, x) - 1;
      }
      ind = val/step + dp/(expp(2, x));
      if (ind > pHeap->end) {
         btmovr = 1;
         val = val + 1;
         distance = 2;
         x = 0;
         step = expp(2, x+1);
         dTrial = expp(2, x) - 1;
         while (val % step != dTrial) {
            x++;
            step = expp(2, x+1);
            dTrial = expp(2, x) - 1;
         }
         ind = val/step + dp/(expp(2, x));
      }
      (*output)[c] = (pHeap->store)[ind-1];
   }
   return 0;
}

int expp(int val, int power) {
   int c, ret = 1;
   if (power == 0) { return 1; }
   for (c=0; c < power; c++) {
      ret = ret*val;
   }
   return ret;
}

int postorder(HeapType *pHeap, int **output, int *o_size) { /* LRN */
   int c = 1, x = 0, val = 0, distance = 0;
   int depth = 0,dp = 0;
   int dTrial = 1;
   int ind = 0;
   int step = 1;
   int btmovr = 0;
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   while (c*2 <= pHeap->end) {
      c *= 2;
      depth++;
   }
   dp = expp(2, depth);
   
   return 0;
}

int print(int val) {
   printf("DEBUG -> %d\n", val);
   return 0;
}

int initOutArray(int size, int **out, int *o_size) {
   int c = 0;
   if (out == NULL || o_size == NULL) { return -1; }
   *out = (int *)malloc(sizeof(int)*size);
   *o_size = size;
   return 0;
}

int getParentIndex(int index) {
   if (index == 0) { return -1; }
   return (int)((index+1) / 2) - 1;
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
   if (pHeap->end + 1 > pHeap->size) {  
      return -1;
   }
   st[(pHeap->end)] = key;
   pHeap->end = pHeap->end + 1;
   return shiftValue(pHeap, pHeap->end-1);
}

int findHeap(HeapType *pHeap, int key) {
   int c;
   if (pHeap == NULL) { return -1; }
   for (c=0; c < pHeap->end; c++) {
      if (key == (pHeap->store)[c]) { return 1; }
   }
   return 0;
}

int delHeap(HeapType *pHeap, int *key) {
   if (pHeap == NULL || key == NULL) { return -1; }
   *key = (pHeap->store)[0];
   moveLargestUp(pHeap, 0);
   pHeap->end = pHeap->end - 1;
   return 0;
}

int moveLargestUp(HeapType *pHeap, int parent) {
   int par = parent + 1;
   int l,r,chosen;
   if (pHeap == NULL) { return -1; }
   if (par*2 >= pHeap->end) {
      return 0;
   } else {
      l = par*2;
      r = (par*2)+1;
      if ((pHeap->store)[l-1] > (pHeap->store)[r-1]) {
         chosen = l;
      } else {
         chosen = r;
      }
      (pHeap->store)[parent] = (pHeap->store)[chosen-1];
      return moveLargestUp(pHeap, chosen-1);
   }
}