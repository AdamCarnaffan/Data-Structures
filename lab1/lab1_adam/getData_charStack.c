#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_head(llnode **x, char value) {
   llnode *newNode = NULL;
   llnode *oldHead = *x;
   if (x==NULL) { return -1; }
   newNode = (llnode *)malloc(sizeof(llnode));
   newNode->value = value;
   newNode->next = oldHead;
   *x = newNode;
   return 0;
}

int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int push(llnode **x, char value) {
   int r = 0;
   /* Don't need to validate x as it is validated in the function call */
   r = llnode_add_to_tail(x, value);
   return r;
}


int pop(llnode **x, char *return_value) {
   if (x==NULL) { return -1; }
   if (return_value == NULL) { return -1; }
   if ((*x)->next == NULL) {
      *return_value = (*x)->value;
      free(*x);
      *x = NULL;
      return 0;
   }
   if (((*x)->next)->next == NULL) {
      *return_value = ((*x)->next)->value;
      free((*x)->next);
      (*x)->next = NULL;
      return 0;
   } else {
      return pop(&((*x)->next), return_value);
   }
   return 0;
}

int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
	 return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
	 return 0;
      }
   }
}

int main(void) {
   int n=0;
   char value=0;
   int rvalue=0;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      n=n+1;
      push(&input_list,value);
   }
   printf("INFO: you entered %d items\n",n);
   while (n > 0) {
      rvalue = pop(&input_list, &value);
      printf("%c\n",value);
      n = n - 1;
   }
   if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); }
   return 0;
}
