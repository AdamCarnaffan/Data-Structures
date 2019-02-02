#include <stdio.h>
#include <stdlib.h>
#include "avlrot.h"

int main(void) {
   avlNode *root = NULL;
   int add = 0;
   while (scanf("%d", &add) != EOF) {
      add_avl(&root, add);
   }
   printTreeInOrder(root);
   printf("Balance is: %d\n", isAVL(&root));
   dblrotate(&root, 1);
   printTreeInOrder(root);
   printf("Balance is: %d\n", isAVL(&root));
   return 0;
}