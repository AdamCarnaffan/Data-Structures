#include <stdio.h>

int bs(int*, int, int *(int, int) );
int lt(int, int);
int gt(int, int);

int bs(int *x, int size, int *compare(int x, int y)) {
   int c = 0;
   int d = 0;
   int swp;
   if (x == NULL || size < 1 || compare == NULL) {
      return -1;
   }
   for (; c < size; c++) {
      for (d=0; d < size; d++) {
         if (compare(x[c], x[d])) {
            swp = x[c];
            x[c] = x[d];
            x[d] = swp;
         }
      }
   }
   return 0;
}

int lt(int x, int y) {
   if (x > y) {
      return 0;
   }
   return 1;
}

int gt(int x, int y) {
   if (x < y) {
      return 0;
   }
   return 1;
}