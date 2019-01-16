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

int push(llnode **x, char new_value) {
   if (x == NULL) {
      return -1;
   }
   return llnode_add_to_tail(x, new_value);
}

int pop(llnode **x, char *return_value) {
   llnode *tail = NULL;
   if ((x == NULL) || (*x == NULL)) {
      *return_value = 0;
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

int llnode_print_from_head(llnode *x) {
   if (x == NULL) { 
   return 0; 
   }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int main(void) {
   int counter = 0;
   int fail = 0;
   int fail_position = -1;
   char input = 0;
   llnode *checker = NULL;
   char left[3] = "({[";
   char right[3] = "]})";
   int i = 0;
   char popped = 0;
   char flip = 0;
   while (scanf("%c", &input) != EOF) {
      counter += 1;
      for (i = 0; i < 3; i++) {
         if (input == left[i]) {
            push(&checker, input);
         }
         else if (input == right[i]) {
            pop(&checker, &popped);
            if (popped == '[') {
               flip = ']';
            }
            else if (popped == '{') {
               flip = '}';
            }
            else if (popped == '(') {
               flip = ')';
            }
            if ((flip != input) && (fail == 0)) {
               fail = 1;
               if (fail_position == -1) {
                  fail_position = counter;
               }
            }
            flip = 0;
         }
      }
   }
   pop(&checker, &popped);
   if ((fail == 0) && (fail_position == -1) && (popped != 0)) {
      printf("Fail, %d\n", counter);
   } 
   else if ((fail == 1) || (fail_position != -1) || (popped != 0)) {
      printf("FAIL, %d\n", fail_position);
   }
   else {
      printf("PASS\n");
   }
   return 0;
}
