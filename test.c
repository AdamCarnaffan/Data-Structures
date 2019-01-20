#include <stdio.h>

typedef struct {
   int *x;
   int end;
   int len;
} intlist;

int x(int *, int *);

int x(int *a, int *z) {
   *a = 5;
   return 0;
}

int main(void) {
   int b = 9;
   int y = 12;
   printf("%d\n", b);
   printf("%d\n", y);
   printf("%d\n", x(&b, &y));
   printf("%d\n", b);
   printf("%d\n", y);
   return 0;
}