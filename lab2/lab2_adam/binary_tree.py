from queue_helper import Queue
import tree as tt

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
      print(ind + str(self.store[0]))
      if self.store[2] != []:
         self.store[2].display(indent+1)
      if self.store[1] != []:
         self.store[1].display(indent+1)
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
         if r[1] != []:
            q.enqueue(r[1].store)
         if r[2] != []:
            q.enqueue(r[2].store)
      return final

   def ConvertToTree_Builder(self):
      t = tt.tree(self.store[0])
      if self.store[1] != []:
         sibs = self.store[1].ConvertToTree()
         t.AddSuccessor(sibs[0])
         for l in sibs[1]:
            t.AddSuccessor(l)
      if self.store[2] != []:
         sibs = self.store[2].ConvertToTree()
         if type(sibs) == list:
            final = [sibs[0]]
            for s in sibs[1]:
               final = final + [s]
            return [t, final]
         else:
            return [t, [sibs]]
      return t

   def ConvertToTree(self):
      if self.store[2] != []:
         return [False, []]
      else:
         return [True, self.ConvertToTree_Builder()]