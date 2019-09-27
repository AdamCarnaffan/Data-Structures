def quick_sort(u, ini, fin):
   if (ini < fin):
      p = partition(u, ini, fin)
      quick_sort(u, ini, p-1)
      quick_sort(u, p + 1, fin)
   return True

def partition(u, ini, fin):
   piv = u[fin]
   v = ini
   for i in range(ini, fin+1, 1):
      if (u[i] < piv):
        swp = u[v]
        u[v] = u[i]
        u[i] = swp
        v = v + 1
   u[fin] = u[v]
   u[v] = piv
   return v

def hanoi(n, start, tmp, final):
   if n > 0:
        hanoi(n - 1, start, [], tmp)
        final.append(start.pop())
        hanoi(n - 1, tmp, start, final)
        return True
   else:
        return True