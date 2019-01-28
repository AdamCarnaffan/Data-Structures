#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

int add_bst(bstNode **root,int new_val);
int printTreeInOrder(bstNode *root);


int add_bst(bstNode **root,int new_val) {
   if (root == NULL) { 
      return -1; 
   }
   else if (*root == NULL) {
      *root = (bstNode *)malloc(sizeof(bstNode));
      (*root)->val = new_val;
      (*root)->l = NULL;
      (*root)->r = NULL;
      return 0;
   }
   else if ((*root)->val == new_val) {
      return -1;
   }
   else if (new_val > (*root)->val) {
      return add_bst(&((*root)->r), new_val);
   }
   else if (new_val < (*root)->val) {
      return add_bst(&((*root)->l), new_val);
   }
}

int printTreeInOrder(bstNode *root) {
   if (root == NULL) {
      return -1;
   }
   if (root->l != NULL) {
      printTreeInOrder(root->l);
   }
   printf("%d\n", root->val);
   if (root->r != NULL) {
      printTreeInOrder(root->r);
   }
   return 0;
}

int main(void) {
   int in_value = 0;
   bstNode *root = NULL;
   while (scanf("%d", &in_value) != EOF) {
      add_bst(&root, in_value);
   }
   printTreeInOrder(root);
   return 0;
}