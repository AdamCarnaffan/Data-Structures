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
