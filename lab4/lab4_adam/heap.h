typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

struct stack {
   int val;
   struct stack *next;
};

typedef struct stack stack;


int initHeap(HeapType *,int);
int initOutArray(int, int **, int *);
int inorder(HeapType *, int **, int *);
int preorder(HeapType *, int **, int *);
int postorder(HeapType *, int **, int *);
int findHeap(HeapType *, int);
int delHeap(HeapType *, int *);
int addHeap(HeapType *, int);
int shiftValue(HeapType *, int);
int getParentIndex(int);
int getLeftIndex(int);
int getRightIndex(int);
int print(int);
int expp(int, int);
int moveLargestUp(HeapType *, int);