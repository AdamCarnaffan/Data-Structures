def sortr(L):
   print(L)
   if len(L) < 1:
      return []
   sub = []
   maxLength = 0
   # Stringify all digits
   for v in L:
      sub = sub + [str(v)]
   # Get rid of negatives on first pass
   neg = []
   pos = []
   for v in sub:
      if v[0] == "-":
         neg = neg + [v[1:len(v)]]
      else:
         pos = pos + [v]
   ints = [pos, neg]
   for v in ints:
      for l in v:
         if len(str(l)) > maxLength:
            maxLength = len(str(l))
   posB = [[]]*10
   negB = [[]]*10
   bucks = [posB, negB]
   for i in range(0, 2, 1):
      for v in ints[i]:
         if len(v) < maxLength:
            bucks[i][0] = bucks[i][0] + [v]
         else:
            bucks[i][int(v[0])] = bucks[i][int(v[0])] + [v[1:len(v)]]
   for i in range(0, 2, 1):
      for l in range(0, 10, 1):
         if (len(bucks[i][l]) > 1 and len(bucks[i][l][0]) >= 1):
            if (i == 1):
               bucks[i][l] = sortr(["-" + str(v) for v in bucks[i][l]])
               bucks[i][l] = [str(v)[1:len(str(v))] for v in bucks[i][l]]
            else:
               bucks[i][l] = sortr(bucks[i][l])
   final = []
   for v in range(9, -1, -1):
      for i in negB[v]:
         final = final + [int("-" + str(v) + str(i))]
   for v in range(0, 10, 1):
      for i in posB[v]:
         final = final + [int(str(v) + str(i))]
   return final

def main():
   print(4 % 3)
   return

main()