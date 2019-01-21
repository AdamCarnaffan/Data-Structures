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

   def display(self, indent):
      ind = ''
      for i in range(0, indent, 1):
         ind = ind + '   '
      print(ind + self.store[0])
      if self.store[2] != []:
         self.store[2].display(indent+1)
      if self.store[1] != []:
         self.store[1].display(indent+1)
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

   def convertToTree(self):
      t = tree(self.store[0])
      if self.store[1] != []:
         sibs = self.store[1].convertToTree()
         t.AddSuccessor(sibs[0])
         for l in sibs[1]:
            t.AddSuccessor(l)
      if self.store[2] != []:
         sibs = self.store[2].convertToTree()
         if type(sibs) == list:
            final = [sibs[0]]
            for s in sibs[1]:
               final = final + [s]
            return [t, final]
         else:
            return [t, [sibs]]
      return t


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

   def convertToBinaryTree_Non(self):
      root = binary_tree(self.store[0])
      newq = Queue()
      for v in self.store[1]:
         newq.enqueue(v)
      targ = root
      childPaths = Queue()
      children = Queue()
      childPaths.enqueue(newq)
      sibs = []
      while len(childPaths.vals) > 0:
         first = True
         rt = childPaths.dequeue()[1]
         while True:
            child = rt.dequeue()
            if child[0] == False:
               break
            t = child[1]
            b = binary_tree(t.store[0])
            if first:
               targ.AddLeft(b)
               branch = b
               first = False
            else:
               sibs = sibs + [b]
            children.enqueue(b)
            newq = Queue()
            for vl in t.store[1]:
               newq.enqueue(vl)
            childPaths.enqueue(newq)
         print(childPaths.vals)
         for v in sibs:
            print(branch.store[0])
            print(v.store[0])
            branch.AddRight(v)
            branch = v
         sibs = []
         targ = children.dequeue()[1]
      return root
      


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
   l.display(0)
   print(l.store[1].store[2].store[2].store[2].store[1].store[0])

main()
