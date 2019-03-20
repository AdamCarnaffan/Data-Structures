#include <stdio.h>
#include <stdlib.h>

unsigned char FSR(unsigned char);
void print_bytes(unsigned char);
unsigned char prng(unsigned char, unsigned char);
int crypt(char *data, unsigned int size, unsigned char password);

int main(void) {
   unsigned int size = 5;
   unsigned char *inp = (unsigned char *)malloc(sizeof(unsigned char)*size);
   inp[0] = 'T';
   inp[1] = 'h';
   inp[2] = 'i';
   inp[3] = 's';
   inp[4] = '\0';
   unsigned char password = 0xb8;
   printf("%s\n", inp);
   crypt(inp, size, password);
   printf("%s\n", inp);
   crypt(inp, size, password);
   printf("%s\n", inp);
   return 0;
}

unsigned char prng(unsigned char x, unsigned char pattern) {
   unsigned char res = FSR(x);
   return res ^ pattern;
}

unsigned char FSR(unsigned char x) {
   unsigned char last = x & 0x1;
   unsigned char r = x >> 1;
   unsigned char newFirst = last << 7;
   r = r | newFirst;
   return r;
}

void print_bytes(unsigned char x) {
   int i = 0;
   int size = sizeof(unsigned char);
   int maxPow = 1<<(size*8-1);
   for (;i<size*8;++i) {
      printf("%u", !!(x&maxPow));
      x = x<<1;
   }
}

int crypt(char *data, unsigned int size, unsigned char password) {
   int c = 0;
   unsigned char prngVal = password;
   if (data == NULL || size < 1 || password == 0x00) {
      return -1;
   }
   for (c=0; c<size; c++) {
      prngVal = prng(prngVal, 0xb8);
      data[c] = (data[c]) ^ prngVal;
   }
   return 0;
 }