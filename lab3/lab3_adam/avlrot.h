struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

int get_depth(avlNode *);
int find_depth(avlNode *);
int measure_balance(avlNode *);
int isAVL(avlNode **);
int add_avl(avlNode **,int);
int rotate(avlNode **, unsigned int);
int printTreeInOrder(avlNode *);
int rotate(avlNode **, unsigned int);
int dblrotate(avlNode **,unsigned int);