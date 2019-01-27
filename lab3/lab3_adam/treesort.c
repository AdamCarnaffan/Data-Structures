#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;


int add_bst(bstNode**, int);
int printTreeInOrder(bstNode *);


int main(void) {
   bstNode *root = NULL;   
   int n = 0;
   int value = 0;

   while (scanf("%d",&value) != EOF) {
      n=n+1;
      add_bst(&root, value);
   }
   printTreeInOrder(root);
   return 0;
}

int add_bst(bstNode **root, int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      *root = (bstNode *)malloc(sizeof(bstNode));
      (*root)->val = val;
      (*root)->r = NULL;
      (*root)->l = NULL;
      return 0;
   } else {
      if (val == (*root)->val) {
         return -1;
      } else if (val > (*root)->val) {
         return add_bst(&((*root)->r), val);
      } else if (val < (*root)->val) {
         return add_bst(&((*root)->l), val);
      }
   }
}

int printTreeInOrder(bstNode *root) {
   if (root == NULL) { return -1; }
   printTreeInOrder(root->l);
   printf("%d\n", root->val);
   printTreeInOrder(root->r);
   return 0; /* Will only return -1 if base case fails */
}