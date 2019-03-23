#include <stdio.h>
#include <stdlib.h>

unsigned int rot(unsigned int, int);

int print(unsigned int x) {
   int i = 0;
   int size = sizeof(unsigned int);
   unsigned int mp = 1<<(size*8-1);
   for (; i<size*8; ++i) {
      printf("%u ", x&mp ? 1 : 0);
      x = x<<1;
   }
   printf("\n");
}

int main(void) {
   printf("%x\n", rot(0xfafa1234, 0));
   return 1;
}

// 60 -> 00111100

unsigned int rot(unsigned int x, int n) {
   int shift = 0;
   int holder = 0;
   int bot = 0;
   int top = 0;
   if (n > 0) {
      shift = n;
      holder = x << 1;
   } else if (n == 0) {
      top = x >> 16;
      bot = x << 16;
      bot = bot >> 16;
      holder = top ^ bot;
      top = top << 16;
      return top | holder;
   } else {
      shift = n*(-1);
   }
   return 0;
}