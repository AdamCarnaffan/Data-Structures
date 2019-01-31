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
int isAVL(avlNode **);
int add_avl(avlNode **,int);
int rotate(avlNode **, unsigned int);
int printTreeInOrder(avlNode *);

int main(void) {
   avlNode *root = NULL;
   int add = 0;
   while (scanf("%d", &add) != EOF) {
      add_avl(&root, add);
   }
   printTreeInOrder(root);
   printf("Balance is: %d\n", isAVL(&root));
   return 0;
}

int add_avl(avlNode **root,int val) {
   if (root == NULL) { 
      return -1; 
   }
   else if (*root == NULL) {
      *root = (avlNode *)malloc(sizeof(avlNode));
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
      (*root)->balance = 0; 
      return 0;
   }
   else if (val > (*root)->val) {
      (*root)->balance += 1;
      return add_avl(&((*root)->r), val);
   }
   else if (val < (*root)->val) {
      (*root)->balance -= 1;
      return add_avl(&((*root)->l), val);
   }
   else {
      return -1;
   }
}

int printTreeInOrder(avlNode *root) {
   if (root == NULL ) {
      return -1;
   }
   printTreeInOrder(root->l);
   printf("val: %d, balance: %d\n", root->val, root->balance);
   printTreeInOrder(root->r);
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
   if (r > l) { 
      final = r; 
   } else { 
      final = l; 
   }
   return final + 1;
}

int isAVL(avlNode **root) {
   int l, r, final;
   if (root == NULL) { return -1; }
   if (*root == NULL) { return 0; }
   final = get_depth((*root)->r) - get_depth((*root)->l);
   if (final < -1 || final > 1) {
      return -1;
   } else {
      l = isAVL(&((*root)->l));
      r = isAVL(&((*root)->r));
      if (r == -1 || l == -1) {
         return -1;
      }
   }
   return 0;
}