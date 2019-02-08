#include <stdlib.h>
#include <stdio.h>
#include "heap.h"

int push(stack **root, int val) {
   stack *cur = *root;
   if (root == NULL) {
      return -1;
   }
   *root = (stack *)malloc(sizeof(stack));
   (*root)->val = val;
   (*root)->next = cur;
}

int pop(stack **root, int *ret) {
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
   int c,ind = 0;
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   stack *s = NULL;
   push(&s, 1);
   for (c=0; c<pHeap->end; c++) {
      if (pop(&s, &ind) == -1) {
         break;
      }
      (*output)[c] = (pHeap->store)[ind-1];
      if (getRightIndex(ind) <= pHeap->end) {
         push(&s, getRightIndex(ind));
      }
      if (getLeftIndex(ind) <= pHeap->end) {
         push(&s, getLeftIndex(ind));
      }
   }
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

int postorder(HeapType *pHeap, int **output, int *o_size) { /* LRN */
   int c,ind = 0;
   if (output == NULL || pHeap == NULL || o_size == NULL) { return -1; }
   initOutArray(pHeap->end, output, o_size);
   stack *s = NULL;
   stack *pr = NULL;
   push(&s, 1);
   for (c=0; c<pHeap->end; c++) {
      if (pop(&s, &ind) == -1) {
         break;
      }
      push(&pr, (pHeap->store)[ind-1]);
      if (getLeftIndex(ind) <= pHeap->end) {
         push(&s, getLeftIndex(ind));
      }
      if (getRightIndex(ind) <= pHeap->end) {
         push(&s, getRightIndex(ind));
      }
   }
   c = 0;
   while (pop(&pr, &ind) != -1) {
      (*output)[c] = ind;
      c++;
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

int delHeap(HeapType *pHeap, int *key) {
   if (pHeap == NULL || key == NULL) { return -1; }
   *key = (pHeap->store)[0];
   moveLargestUp(pHeap, 0);
   pHeap->end = pHeap->end - 1;
   return 0;
}