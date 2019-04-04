def rule(value, array):
   if type(array) != list:
      return False
   total = 0
   for i in array:
      total += i
   if value == 1:
      if total == 2 or total == 3:
         return 1
   else:
      if total == 3:
         return 1
   return 0
