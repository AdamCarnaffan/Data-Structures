#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

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

int bc(llnode **list, char in) {
   char left[3] = "({[";
   char right[3] = "]})";
   int i = 0;
   int j = 0;
   char popped = 0;
   char compare = 0;
   int check_right = 1;
   if (list == NULL) {
      return -1;
   }
   for (i = 0; i < 3; i++) {
      if (left[i] == in) {
         push(list, in);
         return 0;
      }
   }
   for (j = 0; j < 3; j++) {
      if (right[j] == in) {
         pop(list, &popped);
         if (popped == "[") {
            compare = "]";
         }
         else if (popped == "{") {
            compare = "}";
         }
         else if (popped == "(") {
            compare = ")";
         }
         if (compare != in) {
            return -1;
         }
      }
   }
   return 0;
}

int main(void) {
   int count = 0;
   char piece = 0;
   llnode *list = NULL;
   int check = 0;
   int fail = 0;
   int fail_cnt = 0;
   while (scanf("%c", &piece) != EOF) {
      count = count + 1;
      check = bc(&list, piece);
      if (check == -1) {
         fail = 1;
         break;
      }
   }
   if ((fail == 1) || (piece != 0)) {
      printf("FAIL, %d\n", count);
   }
   else {
      printf("PASS\n");
   }
   return 0;
}
