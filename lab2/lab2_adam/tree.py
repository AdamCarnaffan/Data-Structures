from queue_helper import Queue


class binary_tree:
   def __init__(self, x):
      self.store = [x, [], []] # Val, left, right -> left = Child -> right = Sibling

   def AddLeft(self, val):
      if self.store[1] != []:
         return False
      self.store[1] = val
      return True

   def AddRight(self, val):
      if self.store[2] != []:
         return False
      self.store[2] = val
      return True

   def Get_LevelOrder(self):
      q = Queue()
      q.enqueue(self.store)
      final = []
      while len(q.vals) > 0:
         r = q.dequeue()[1]
         final = final + [r[0]]
         if r[1] != []:
            q.enqueue(r[1].store)
         if r[2] != []:
            q.enqueue(r[2].store)
      return final


class tree:
   def __init__(self, x):
      self.store = [x, []]

   def AddSuccessor(self, x):
      self.store[1] = self.store[1] + [x]
      return True

   def display(self, indent):
      ind = ''
      for i in range(0, indent, 1):
         ind = ind + '   '
      print(ind + self.store[0])
      for t in self.store[1]:
         t.display(indent+1)
      return True

   def Get_LevelOrder(self):
      q = Queue()
      q.enqueue(self.store)
      final = []
      while len(q.vals) > 0:
         r = q.dequeue()[1]
         final = final + [r[0]]
         for i in r[1]:
            q.enqueue(i.store)
      return final

   def convertToBinaryTree(self, sibs=[]):
      b = binary_tree(self.store[0])
      if len(self.store[1]) > 0:
         b.AddLeft(self.store[1][0].convertToBinaryTree(self.store[1][1:len(self.store[1])]))
      if len(sibs) > 0:
         b.AddRight(sibs[0].convertToBinaryTree(sibs[1:len(sibs)]))
      return b
      


def main():
   a = tree("texmf")
   a.AddSuccessor(tree("doc"))
   a.AddSuccessor(tree("fonts"))
   a.AddSuccessor(tree("source"))
   b = tree("tex")
   b.AddSuccessor(tree("generic"))
   b.AddSuccessor(tree("latex"))
   b.AddSuccessor(tree("plain"))
   a.AddSuccessor(b)
   a.AddSuccessor(tree("texdoc"))
   #print(a.Get_LevelOrder())
   l = a.convertToBinaryTree()
   print(l.Get_LevelOrder())

main()
