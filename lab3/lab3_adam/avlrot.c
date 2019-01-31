#include <stdio.h>
#include <stdlib.h>

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

int get_depth(avlNode *);
int find_depth(avlNode *);
int measure_balance(avlNode *);

int main(void) {

   return 0;
}

int get_depth(avlNode *root) {
   return find_depth(root) - 1;
}

int find_depth(avlNode *root) {
   int l, r, final;
   if (root == NULL) {
      return 0;
   }
   l = find_depth(root->l);
   r = find_depth(root->r);
   if (r > l) { final = r; } else { final = l; }
   return final + 1;
}