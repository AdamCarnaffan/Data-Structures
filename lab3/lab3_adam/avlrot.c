#include <stdio.h>
#include <stdlib.h>
#include "avlrot.h"

int add_avl(avlNode **root,int val) {
   if (root == NULL) { 
      return -1; 
   } 
   if (*root == NULL) {
      *root = (avlNode *)malloc(sizeof(avlNode));
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
      (*root)->balance = 0; 
      return 0;
   } else if (val > (*root)->val) {
      (*root)->balance = (*root)->balance + 1;
      return add_avl(&((*root)->r), val);
   } else if (val < (*root)->val) {
      (*root)->balance = (*root)->balance - 1;
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

int compute_balance(avlNode *root) {
   root->balance = get_depth(root->r) - get_depth(root->l);
   return 0;
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

int rotate(avlNode **root, unsigned int Left0_Right1) {
   avlNode *branch = NULL; /* will be new root */
   avlNode *save = NULL;
   avlNode *org = *root;
   if (root == NULL) { return -1; }
   if (Left0_Right1 == 1) {
      if ((*root)->l == NULL) { return -1; }
      branch = (*root)->l;
      save = branch->r;
      (*root)->l = save;
      branch->r = (*root);
      (*root) = branch;
   } else { 
      if ((*root)->r == NULL) { return -1; }
      branch = (*root)->r; 
      save = branch->l;
      (*root)->r = save;
      branch->l = (*root);
      (*root) = branch;
   }
   compute_balance(branch);
   compute_balance(org);
   return 0;
}

int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1) {
   if (root == NULL) { return -1; }
   if (MajLMinR0_MajRMinL1 == 1) {
      if ((*root)->r == NULL) { return -1; }
      rotate(&((*root)->r), 1);
      rotate(root, 0);
   } else {
      if ((*root)->l == NULL) { return -1; }
      rotate(&((*root)->l), 0);
      rotate(root, 1);
   }
   return 0;
}