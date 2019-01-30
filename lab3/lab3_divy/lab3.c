#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

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

int add_bst(bstNode **root,int new_val);
int printTreeInOrder(bstNode *root);
int printLevelOrder(bstNode *root);

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
   printTreeInOrder(root->l);
   printf("%d\n", root->val);
   printTreeInOrder(root->r);
   return 0;
}

int printLevelOrder(bstNode *root) {  /* does not work as intended */
   if (root == NULL) {
      return -1;
   }
   queue *q = (queue *)malloc(sizeof(queue));
   bstNode *item = NULL;
   enqueue(&q, root);
   while (len_queue(q)) {
      dequeue(&q, item);
      printf("%d ", item->val);
      if (item->l != NULL) {
         enqueue(&q, item->l);
      }
      if (item->r != NULL) {
         enqueue(&q, item->r);
      }
   }
   return 0;
}

int main(void) {
   bstNode *root = NULL;
   add_bst(&root, 5);
   add_bst(&root, 3);
   add_bst(&root, 1);
   add_bst(&root, 4);
   add_bst(&root, 7);
   add_bst(&root, 6);
   add_bst(&root, 8);
   printTreeInOrder(root);
   printf("\n");
   printLevelOrder(root);
   printf("\n");
   return 0;
}