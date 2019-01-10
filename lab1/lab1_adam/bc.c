#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

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
   if (*x == NULL) {
      *return_value = 0;
      return -1;
   }
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

int main(void) {
   int n = 0;
   char value = 0;
   char popped_value = 0;
   char comp = 0;
   int rvalue = 0;
   int result = 0;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      n = n + 1;
      if (value == '(' || value == '[' || value == '{') {
         rvalue = push(&input_list, value);
      } else if (value == ')' || value == ']' || value == '}') {
         rvalue = pop(&input_list, &popped_value);
         if (value == ')') {
            comp = '(';
         } else if (value == ']') {
            comp = '[';
         } else {
            comp = '{';
         }
         if (comp != popped_value) {
            result = -1;
            break;
         }
         comp = ' '; /* Reset the variable */
      }
   }
   /* Check if values remain on the stack */
   if (pop(&input_list, &popped_value) == 0) {
      result = -1;
   }
   if (result == 0) {
      printf("PASS\n");
   } else {
      printf("FAIL,%d\n", n);
   }
   return 0;
}
