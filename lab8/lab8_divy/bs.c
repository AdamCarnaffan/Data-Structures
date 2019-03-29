#include <stdio.h>
#include <stdlib.h>

int lt(int x, int y);
int gt(int x, int y);
int bs(int *array, int array_size, int (*compare)(int x, int y));


int lt(int x, int y) {
   if (x > y) {
      return 1;
   }
   return 0;
}

int gt(int x, int y) {
   if (x < y) {
      return 1;
   }
   return 0;
}

int bs(int *array, int array_size, int (*compare)(int x, int y)) {
   if ((array == NULL) || (*compare == NULL)) {
      return -1;
   }
   int i = 0, j = 0, swapped_flag = 0, swapper = 0;
   for (i = 0; i < array_size - 1; i++) {  // do not need to go to last index
      swapped_flag = 0;
      for (j = 0; j < array_size - i - 1; j++) {  // ith index from the end is sorted
         if ((*compare)(array[j], array[j + 1]) == 1) {
            swapper = array[j];
            array[j] = array[j + 1];
            array[j + 1] = swapper;
            swapped_flag = 1;
         }
      }
      if (swapped_flag == 0) {
         break;
      }
   }
   return 0;
}


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