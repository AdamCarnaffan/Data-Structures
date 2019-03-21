#include <stdio.h>
#include <stdlib.h>

unsigned char FSR(unsigned char x);  /* feedback shift register */
unsigned char prng(unsigned char x, unsigned char pattern);  /* pseudo-random number generator */
int crypt(char *data, unsigned int size, unsigned char password);

unsigned char FSR(unsigned char x) {
   unsigned char bit0 = x & 0x1; /* extract bit 0 */
   bit0 <<= 7; /* move bit0 to the bit7 pos */
   x >>= 1;        /* shift right   */
   x |= bit0; /* rotate the old value of bit 0 into the bit 7 pos */
   return x;
}

unsigned char prng(unsigned char x, unsigned char pattern) {
   x = FSR(x);
   return x ^= pattern;
}

int crypt(char *data, unsigned int size, unsigned char password) {  /* size is one extra because of '\0' at the end */
   if ((password == 0x0) || (size <= 1) || (data == NULL)) {
      return -1;
   }
   int i = 0;
   for (i = 0; i < size - 1; i++){
      password = prng(password, 0xb8);
      data[i] = data[i] ^ password;
   }
   return 0;
}

int main(void) {
   unsigned char x = 0x1;
   int i = 0;
   int j = 0;
   char S[3];
   S[0] = 'a';
   S[1] = 'b';
   S[2] = '\0';
   printf("\n\nFOR LOOP\n");
   for (i = 0; i < 10; i++) {
      crypt(S, 3, 0x77);
      for (j = 0; j < 2; j++) {
         printf("%c ", S[j]);
      }
      printf("\n");
   }
   return 0;

}