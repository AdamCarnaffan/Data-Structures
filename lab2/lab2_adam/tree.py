from queue_helper import Queue
import binary_tree as bt

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
      print(ind + str(self.store[0]))
      for t in self.store[1]:
         t.display(indent+1)
      return True

   def Get_DepthFirst(self):
      return self.display(0)

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

   def ConvertToBinary_Builder(self, sibs):
      b = bt.binary_tree(self.store[0])
      if len(self.store[1]) > 0:
         b.AddLeft(self.store[1][0].ConvertToBinary_Builder(self.store[1][1:len(self.store[1])]))
      if len(sibs) > 0:
         b.AddRight(sibs[0].ConvertToBinary_Builder(sibs[1:len(sibs)]))
      return b

   def ConvertToBinaryTree(self):
      return self.ConvertToBinary_Builder([])

   def ConvertToBinaryTree_Non(self):
      root = bt.binary_tree(self.store[0])
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
            b = bt.binary_tree(t.store[0])
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
      