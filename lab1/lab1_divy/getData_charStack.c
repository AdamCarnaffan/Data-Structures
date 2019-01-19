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
      return 1;
   }
   new_head = (llnode *)malloc(sizeof(llnode));
   new_head->value = new_value;
   new_head->next = *x;  /* if *x is NULL, than next just points to NULL */
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
   } 
   else {
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

int push(llnode **x, char new_value) {
   if (x == NULL) {
      return -1;
   }
   return llnode_add_to_tail(x, new_value);
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
   int counter = 0;
   char value = 0;
   char popped = 0;
   int checker = -1;
   llnode *input_list = NULL;
   while (scanf("%c", &value) != EOF) {
      counter = counter + 1;
      push(&input_list, value);
   }
   printf("INFO: you entered %d items\n", counter);
   checker = llnode_print_from_head(input_list);
   if ( checker != 0) { 
      printf("ERR: llnode_print returned an error\n"); 
   }
   while (counter != 0) {
      pop(&input_list, &popped);
      printf("The return popped char is: %c\n", popped);
      counter -= 1;
   } 
   checker = llnode_print_from_head(input_list);
   if ( checker != 0) { 
      printf("ERR: llnode_print returned an error\n"); 
   }
   return 0;
}
