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

int isAVL(avlNode **root);

int isAVL(avlNode **root) {
    avlNode *depth_finder = NULL;
    if (root == NULL) {
        return -1;
    }
    depth_finder = *root;
    while (depth_finder->l != NULL) {
        (*root)->balance -= 1;
        depth_finder = depth_finder->l
    }
    return 0;
}