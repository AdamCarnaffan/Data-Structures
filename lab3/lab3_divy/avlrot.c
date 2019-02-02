#include <stdio.h>
#include <stdlib.h>

struct avlNode {
   int balance;  /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {  /* never used */
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

int add_avl(avlNode **root, int new_val);
int printTreeInOrder(avlNode *root);
int node_balance(avlNode **root);  /* helper function for: function isAVL */  
int isAVL(avlNode **root);
int rotate(avlNode **root, unsigned int Left0_Right1);


int add_avl(avlNode **root,int new_val) {  /* need to add balance checks */ 
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
      printf("root: %d\n", (*root)->balance);
      add_avl(&((*root)->r), new_val);
   }
   else if (new_val < (*root)->val) {
      (*root)->balance -= 1;
      printf("root: %d\n", (*root)->balance);
      add_avl(&((*root)->l), new_val);
   }
   else if (new_val == (*root)->val) {
      return -1;
   }
   else {
      return 0;
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

int node_depth(avlNode **root) { 
   int depth = 0;
   if (root == NULL) {
      return -1;
   }
   else if (*root == NULL) {
      return 0;
   }
   if ((*root)->l != NULL) {
      depth = -1 - abs(node_depth(&((*root)->l)));
   }
   if ((*root)->r != NULL) {
      depth += 1 + abs(node_depth(&((*root)->r)));
   }
   return depth;
}

int isAVL(avlNode **root) {
   int lr = 0;
   if (root == NULL) {
      return -1;
   } 
   else if (*root == NULL) {
      return 0;
   }
   lr = node_depth(root);
   if ((abs(lr) <= 1) && (isAVL(&((*root)->l)) == 0) && (isAVL(&((*root)->r)) == 0)) {
      return 0;
   } 
   else {
      return -1;
   }
}

int rotate(avlNode **root, unsigned int Left0_Right1) {
   
   if ((root == NULL) || (*root == NULL)) {
      return -1;
   }
   
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