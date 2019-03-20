def heap_sort(u): # Use max heap to make ASC order
   heapify(u)
   for ind in range(len(u)-1, -1, -1):
      
      reheapify(u, ind-1)
   pass

def heapify(u):
   final = []
   for ind in range(0, len(u), 1):
      final = final + [u[ind]]
      curPos = ind
      while helper_shift(final, curPos):
         curPos = helper_get_parent(curPos)
   for ind in range(0, len(u), 1):
      u[ind] = final[ind]
   return True

def helper_shift(u, pos):
   if pos > len(u)-1 or len(u) < 2 or pos == 0:
      return False
   par = helper_get_parent(pos)
   if par < 0:
      return False
   if u[par] < u[pos]:
      temp = u[par]
      u[par] = u[pos]
      u[pos] = temp
      return True
   return False

def helper_unshift(u, pos):
   pass

def helper_get_parent(ind):
   if ind == 0:
      return -1
   else:
      return int((ind-1)/2)

def reheapify(u, end):
   pass

def main():
   v = [1, 6, 8, 2]
   heapify(v)
   print(v)
   return

main()