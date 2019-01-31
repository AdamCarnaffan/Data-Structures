#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

struct bst_queueNode {
   bstNode *val;
   struct bst_queueNode *next;
};
typedef struct bst_queueNode bst_queue;


int add_bst(bstNode**, int);
int printTreeInOrder(bstNode *);
int printLevelOrder(bstNode *root);
int push(bst_queue **targ, bstNode *val);
int get_depth(bstNode *);
int find_depth(bstNode *);
bstNode * pop(bst_queue **targ);

int main(void) {
   bstNode *root = NULL;
   add_bst(&root,5);
   add_bst(&root,3);
   add_bst(&root,1);
   add_bst(&root,4);
   add_bst(&root,7);
   add_bst(&root,6);
   add_bst(&root,8);
   printTreeInOrder(root);
   printLevelOrder(root);
   return 0;
}

int push(bst_queue **targ, bstNode *val) {
   if (targ == NULL) { return -1; }
   if (*targ == NULL) {
      (*targ) = (bst_queue *)malloc(sizeof(bst_queue));
      (*targ)->val = val;
      (*targ)->next = NULL;
   } else {
      push(&((*targ)->next), val);
   }
   return 0;
}

bstNode * pop(bst_queue **targ) {
   bstNode *temp = NULL;
   bst_queue *old = NULL;
   if (targ == NULL || *targ == NULL) { return NULL; }
   temp = (*targ)->val;
   old = *targ;
   *targ = old->next;
   free(old);
   old = NULL;
   return temp;
}

int get_depth(bstNode *root) {
   return find_depth(root) - 1;
}

int find_depth(bstNode *root) {
   int l, r, final;
   if (root == NULL) {
      return 0;
   }
   l = find_depth(root->l);
   r = find_depth(root->r);
   if (r > l) { final = r; } else { final = l; }
   return final + 1;
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

int printLevelOrder(bstNode *root) {
   if (root == NULL) { return -1; }
   bst_queue *q = NULL;
   bstNode* branch = NULL;
   push(&q, root);
   while (branch = pop(&q)) {
      printf("%d ", branch->val);
      if (branch->l != NULL) {
         push(&q, branch->l);
      }
      if (branch->r != NULL) {
         push(&q, branch->r);
      }
   }
   printf("\n");
   return 0;
}