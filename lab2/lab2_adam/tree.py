def sort_lists_by_length(l):
   res = list(l)
   for x in range(0, len(l), 1):
      for y in range(0, len(l), 1):
         if len(res[x]) > len(res[y]):
            temp = res[x]
            res[x] = res[y]
            res[y] = temp
   return res


class Queue:
   def __init__(self):
      self.vals = []

   def push(self, x):
      self.vals = self.vals + [x]
      return True

   def pop(self):
      if len(self.vals) < 1:
         return [False, []]
      val = self.vals[0]
      self.vals = self.vals[1:len(self.vals)]
      return [True, val]


class binary_tree:

   def __init__(self, x):
      self.store = [x]


class tree:
   def __init__(self, x):
      self.store = [x, []]

   def AddSuccessor(self, x):
      self.store[1] = self.store[1] + [x]
      return True

   def Print_DepthFirst(self):
      disp = ""
      for val in self.store[1]:
         disp = disp + "   " + str(val.store[0])
      print(disp)
      return True

   def Get_LevelOrder(self):
      t = Queue()
      t.push(self.store)
      strct = []
      while True:
         result = t.pop()
         if not result[0]:
            break
         store = result[1]
         strct = strct + [store[0]]
         for l in store[1]:
            t.push(l.store)
      return strct


def main():
   a = tree(5)
   b = tree(9)
   e = tree(4)
   a.AddSuccessor(e)
   e.AddSuccessor(tree(12))
   a.AddSuccessor(b)
   b.AddSuccessor(tree(3))
   # a.Print_DepthFirst()
   print(a.Get_LevelOrder())

main()
