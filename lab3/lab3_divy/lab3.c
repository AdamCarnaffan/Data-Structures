#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

struct avlNode {
   int balance;  /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

int add_bst(bstNode **root,int new_val) {
   if (root == NULL) { 
      printf("add_bst returned -1 due to NULL\n");
      return -1; 
   }
   else if (*root == NULL) {
      *root = (bstNode *)malloc(sizeof(bstNode));
      (*root)->val = new_val;
      return 0;
   }
   else if ((*root)->val == new_val) {
      return -1;
   }
   else if (new_val > (*root)->val) {
      return add_bst(&((*root)->r), new_val);
   }
   else {
      return add_bst(&((*root)->l), new_val);
   }
}

int printTreeinOrder(root) {
   
}

int main(void) {
   bstNode *root=NULL;
   add_bst(&root,5);
   add_bst(&root,3);
   add_bst(&root,1);
   add_bst(&root,4);
   add_bst(&root,7);
   add_bst(&root,6);
   add_bst(&root,8);
   //printTreeInOrder(root);
   //printLevelOrder(root);
   return 0;
}