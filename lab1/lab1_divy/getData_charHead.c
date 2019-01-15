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

int main(void) {
   int counter = 0;
   char value = 0;
   int checker = 0;
   llnode *input_list = NULL;
   while (scanf("%c", &value) != EOF) {  /* EOF is ctrl-z on windows */
      counter += 1;
      llnode_add_to_head(&input_list, value);
   }
   printf("INFO: you entered %d items\n", counter);
   checker = llnode_print_from_head(input_list);
   if ( checker != 0) { 
      printf("ERR: llnode_print returned an error\n"); 
   }
   return 0;
}
