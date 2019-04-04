def rule(val, alist):
   store = 0
   for num in alist:
      store += num
   if (val == 1):
      if (store == 2) or (store == 3):
         return 1
      else:
         return 0
   else:
      if (store == 3):
         return 1
      else:
         return 0
