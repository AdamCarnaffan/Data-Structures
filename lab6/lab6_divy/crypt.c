#include <stdio.h>
#include <stdlib.h>

unsigned char FSR(unsigned char *);
unsigned char prng(unsigned char x, unsigned char pattern);


unsigned char FSR(unsigned char *x) {
   unsigned char ob0 = *x & 0x1; /* extract bit 0 */
   (*x) >>= 1;        /* shift right   */
   unsigned char nb7 = ob0 << 7; /* move bit0 to the bit7 pos */
   *x |= nb7; /* rotate the old value of bit 0 into the bit 7 pos */
   return 0;
}

unsigned char prng(unsigned char x, unsigned char pattern) {
   return 0;
}

int main(void) {
   unsigned char x = 1;
   printf("byte of unsigned char *var: %d\n", sizeof(x));
   for (int i = 0; i < 8*3; i++) {
      unsigned char new_x = FSR(&x);
      printf("%d\n", x);
   }
   return 0;
}