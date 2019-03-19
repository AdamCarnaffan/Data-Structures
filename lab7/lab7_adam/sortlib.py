def selection_sort(u):
   for x in range(0, len(u), 1):
      selected = x
      for y in range(x+1, len(u), 1):
         if u[selected] > u[y]:
            selected = y
      swp = u[x]
      u[x] = u[selected]
      u[selected] = swp
      print(u)
   return True

def heapify(u):

   return True

def reheapify(u, end):
   return True

def heap_sort(u):

   return True

def merge_sort(u):
   return True

def quick_sort(u, ini, fin):

   return True

def partition(u, ini, fin):
   pIndex = []
   return pIndex

def main():
   u = [5,3,2,1,7]
   selection_sort(u)
   print(u)
   return


main()