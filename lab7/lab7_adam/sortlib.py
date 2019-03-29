def selection_sort(u):
   for x in range(0, len(u), 1):
      selected = x
      for y in range(x+1, len(u), 1):
         if u[selected] > u[y]:
            selected = y
      swp = u[x]
      u[x] = u[selected]
      u[selected] = swp
   return True

def heap_sort(u): # Use max heap to make ASC order
   heapify(u)
   for ind in range(len(u)-1, -1, -1):
      swp = u[0]
      u[0] = u[ind]
      u[ind] = swp
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

def reheapify(u, end):
   keep = u[end+1:len(u)]
   heap = u[0:end+1]
   heapify(heap)
   for v in range(0, len(heap), 1):
      u[v] = heap[v]
   for i in range(0, len(keep), 1):
      u[len(heap) + i] = keep[i]
   return True

def merge_sort(u):
   part = 1
   while part < len(u):
      for select in range(0, int(len(u)/part), 2):
         x = select*part
         y = (select+1)*part
         if y >= len(u):
            break
         wk = []
         while x < (select+1)*part or (y < (select+2)*part and y < len(u)):
            if y >= (select+2)*part or y >= len(u): 
               # Add x
               wk = wk + [u[x]]
               x = x + 1
            elif x >= (select+1)*part:
               # Add y
               wk = wk + [u[y]]
               y = y + 1
            else:
               if u[x] < u[y]:
                  # Add x
                  wk = wk + [u[x]]
                  x = x + 1
               else:
                  # Add y
                  wk = wk + [u[y]]
                  y = y + 1
         for ind in range(select*part, (select+2)*part, 1):
            if ind >= len(u):
               break
            u[ind] = wk[ind - select*part]
      part = part * 2
   return True

def quick_sort(u, ini, fin):

   return True

def partition(u, ini, fin):
   pIndex = []
   return pIndex

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

def helper_get_parent(ind):
   if ind == 0:
      return -1
   else:
      return int((ind-1)/2)

def dumb_sort(u):
   m = []
   last = None
   for i in range(0, len(u), 1):
      poss = None
      trackCnt = 0
      for v in range(0, len(u), 1):
         if (poss == None or u[v] < poss):
            if len(m) == 0:
               poss = u[v]
            elif u[v] > m[i-1]:
               poss = u[v]
            elif u[v] == m[i-1]:
               trackCnt = trackCnt + 1
               if trackCnt == lastCnt + 1:
                  poss = u[v]
      m = m + [poss] 
      if last == poss:
         lastCnt = lastCnt + 1
      else:
         lastCnt = 1
      last = poss
   # Set
   for i in range(0, len(u), 1):
      u[i] = m[i]
   return

def main():
   v1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
   v2 = [100, 1, 1000, 9, 8, 7, 2, 2000, 10]
   v3 = [100, 10, 1000, 9, 8, 7, 2, 6, 5, 2, 3, 1]

   print("SELECTION_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      selection_sort(x)
      print(x)
   
   print("\nMERGE_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      merge_sort(x)
      print(x)

   print("\nHEAP_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      heap_sort(x)
      print(x)
   
   print("\nDUMB_SORT:")
   for i in [v1, v2, v3]:
      x = list(i)
      dumb_sort(x)
      print(x)
   
   # print("\nQUICK_SORT:")
   # for i in [v1, v2, v3]:
   #    x = list(i)
   #    quick_sort(x, 0, len(x) - 1)
   #    print(x)
   return True

main()