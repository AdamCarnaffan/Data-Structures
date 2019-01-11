#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_head(llnode **x, char new_value) {
   llnode *new_head = NULL;
   if (x == NULL) {
      return -1;
   }
   if (*x == NULL) {
      *x = (llnode *)malloc(sizeof(llnode));
      (*x)->value = new_value;
      (*x)->next = NULL;
      return 0;
   }
   new_head = (llnode *)malloc(sizeof(llnode));
   new_head->next = *x;
   new_head->value = new_value;
   *x = new_head;
   return 0;
}

int llnode_add_to_tail(llnode **x, char value) {
   if (x == NULL) { 
      return -1; 
   }
   if (*x == NULL) {
      *x = (llnode *)malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_print_from_head(llnode *x) {
   if (x == NULL) { 
	return 0; 
	}
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x == NULL) { 
	return 0; 
	}
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

int push(llnode **x, char value) {
   int pusher = 0;
   if (x == NULL) {
      return -1;
   }
   return llnode_add_to_tail(x, value);
}

int pop(llnode **x, char *return_value) {
   llnode *tail = NULL;
   if ((x == NULL) && (*x == NULL)) {
      return -1;
   }
   else if ((*x)->next == NULL) {
      *return_value = (*x)->value;
      free(*x);
      *x = NULL;
      return 0;
   }
   tail = *x;
   while (tail->next->next != NULL) {
      tail = tail->next;
   }
   *return_value = tail->next->value;
   free(tail->next);
   tail->next = NULL;
   return 0;
}

int main(void) {
   int n = 0;
   char value = 0;
   char pop_char = 0;
   int rvalue = 0;
   llnode *input_list = NULL;
   while (scanf("%c", &value) != EOF) {
      n = n + 1;
      push(&input_list, value);
   }
   llnode_print_from_head(input_list);
   printf("INFO: you entered %d items\n", n);
   while (n != 0) {
      pop(&input_list, &pop_char);
      printf("The return popped char is: %c\n", pop_char);
      n = n - 1;
   } 
   /* rvalue = llnode_print_from_head(input_list);
   if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); } */

   return 0;
}
