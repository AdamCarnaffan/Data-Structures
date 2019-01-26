#include <stdio.h>
#include <stdlib.h>

struct bstNode {
    int val;
    struct bstNode *l;
    struct bstNode *r;
};
typedef struct bstNode bstNode


int add_bst(bstNode**, int);
int display_bst(bstNode *);
int display_bst_helper(bstNode *, int); 


int main(void) {

    return 0;
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

int display_bst(bstNode *root) {
    return display_bst_helper(root, 0);
}

int display_bst_helper(bstNode *root, int indent) {
    if (root == NULL || *root == NULL) { return -1; }
    int i = 0;
    for (i=0; i < indent*3, i++) {
        printf(" ");
    }
    printf("%d\n", (*root)->val);
    display_bst_helper((*root)->l, indent+1);
    display_bst_helper((*root)->r, indent+1);
    return 0; /* Will only return -1 if base case fails */
}