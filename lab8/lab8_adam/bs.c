#include <stdio.h>

int bs(int*, int, int *(int, int) );
int lt(int, int);
int gt(int, int);

int main(void) {
   int i = 0;
   int vals[10];
   for (i = 0; i < 10; i++) {
      vals[i] = 100 - i;
   }
   printf("\n"); bs(vals, 10, lt);
   for (i = 0; i < 10; i++) {
      printf("in[%d] = %d\n", i, vals[i]);
   }
   printf("\n"); bs(vals, 10, gt);
   for (i = 0; i < 10; i++) {
      printf("out[%d] = %d\n", i, vals[i]);
   }
   return 0;
}

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