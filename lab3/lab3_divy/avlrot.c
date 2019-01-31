#include <stdio.h>
#include <stdlib.h>

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

int add_avl(avlNode **root,int new_val);
int isAVL(avlNode **root);
int printTreeInOrder(avlNode *root);

int add_avl(avlNode **root,int new_val) {
   if (root == NULL) { 
      return -1; 
   }
   else if (*root == NULL) {
      *root = (avlNode *)malloc(sizeof(avlNode));
      (*root)->val = new_val;
      (*root)->l = NULL;
      (*root)->r = NULL;
      (*root)->balance = 0; 
      return 0;
   }
   else if (new_val > (*root)->val) {
      (*root)->balance += 1;
      return add_avl(&((*root)->r), new_val);
   }
   else if (new_val < (*root)->val) {
      (*root)->balance -= 1;
      return add_avl(&((*root)->l), new_val);
   }
   else {
      return -1;
   }
}

int isAVL(avlNode **root) {
   int balance = 0;
   if (root == NULL) {
      return -1;
   }
   else if (*root == NULL) {
      return 0;
   }
   if ((*root)->l != NULL) {
      balance = -1 + isAVL(&((*root)->l));
   }
   if ((*root)->r != NULL) {
      balance += 1 + isAVL(&((*root)->r));
   }
   if ((abs(balance) <= 1) && (isAVL(&(*root)->l)) && (isAVL(&(*root)->r)) != -1)  {
      return 0;
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

int main(void) {
   avlNode *root = NULL;
   int add = 0;
   while (scanf("%d", &add) != EOF) {
      add_avl(&root, add);
   }
   printTreeInOrder(root);
   printf("Balance is: %d", isAVL(&root));
   return 0;
}