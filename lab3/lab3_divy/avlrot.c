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
int node_height(avlNode *root);  /* height finder */  
int isAVL(avlNode **root);
int rotate(avlNode **root, unsigned int Left0_Right1);
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1);
int update_balance(avlNode *root);


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
      add_avl(&((*root)->r), new_val);
      (*root)->balance = node_height(*root);
   }
   else if (new_val < (*root)->val) {
      add_avl(&((*root)->l), new_val);
      (*root)->balance = node_height(*root);
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

int node_height(avlNode *root) { 
   int l = 0, r = 0;
   if (root == NULL) {
      return 0;
   }
   if (root->l != NULL) {
      l = 1 + abs(node_height(root->l));
   }
   if (root->r != NULL) {
      r = 1 + abs(node_height(root->r));
   }
   return r-l;
}

int isAVL(avlNode **root) {
   int lr = 0;
   if (root == NULL) {
      return -1;
   } 
   else if (*root == NULL) {
      return 0;
   }
   (*root)->balance = node_height(*root);
   if ((abs((*root)->balance) <= 1) && (isAVL(&((*root)->l)) == 0) && (isAVL(&((*root)->r)) == 0)) {
      return 0;
   } 
   else {
      return -1;
   }
}

int rotate(avlNode **root, unsigned int Left0_Right1) {
   avlNode *b = NULL;
   if ((root == NULL) || (*root == NULL)) {
      return -1;
   }
   if (Left0_Right1 == 0) {
      if ((*root)->r == NULL) {
         return -1;
      }
      b = (*root)->r;
      (*root)->r = b->l;
      b->l = *root;
      *root = b;
   }
   else if (Left0_Right1 == 1) {
      if ((*root)->l == NULL) {
         return -1;
      }
      b = (*root)->l;
      (*root)->l = b->r;
      b->r = *root;
      *root = b;
   }
   else {
      return -1;
   }
   return 0;
}

int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1) {
   if ((root == NULL) || (*root == NULL)) {
      return -1;
   }
   else if (MajLMinR0_MajRMinL1 == 0) {
      if ((*root)->l == NULL) {
         return -1;
      }
      rotate(&((*root)->l), 0);
      rotate(&(*root), 1);
   }
   else if (MajLMinR0_MajRMinL1 == 1) {
      if ((*root)->r == NULL) {
         return -1;
      }
      rotate(&((*root)->r), 1);
      rotate(&(*root), 0);
   }
   else {
      return -1;
   }
   return 0;
}

int update_balance(avlNode *root) {
   if (root == NULL) {
      return 0;
   }
   root->balance = node_height(root);
   update_balance(root->l);
   update_balance(root->r);
   return 0;
}
