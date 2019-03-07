class Queue:
   def __init__(self):
      self.vals = []

   def enqueue(self, x):
      self.vals = self.vals + [x]
      return True

   def dequeue(self):
      if len(self.vals) < 1:
         return [False, []]
      val = self.vals[0]
      self.vals = self.vals[1:len(self.vals)]
      return [True, val]

class graph:

   def __init__(self):
      self.adj = []
      self.explored = []

   def addVertex(self, n):
      for _ in range(0, n, 1):
         self.adj = self.adj + [[]]
      return len(self.adj)
   
   def addEdge(self, from_idx, to_idx, directed, weight):
      if weight == 0:
         return False
      if from_idx < 0 or to_idx < 0:
         return False
      if from_idx >= len(self.adj) or to_idx >= len(self.adj):
         return False
      # Start Doing Stuff
      self.adj[from_idx] = self.adj[from_idx] + [[to_idx, weight]]
      if not directed:
         self.adj[to_idx] = self.adj[to_idx] + [[from_idx, weight]]
      return True
   
   def doDepth(self, node):
      final = [node]
      self.explored = self.explored + [node]
      for v in self.adj[node]:
         if v[0] not in self.explored:
            final = final + self.doDepth(v[0])
      return final

   def get_first_non_explored(self):
      fnd = True
      for v in range(0, len(self.adj), 1):
         fnd = True
         for i in self.explored:
            if v == i:
               fnd = False
               break
         if fnd:
            return v
      return -1

   def traverse(self, start, typeBreadth):
      root = start if start != None else 0
      self.explored = []
      dp = []
      if not typeBreadth:
         if start == None:
            while True:
               dp = dp + [self.doDepth(root)]
               root = self.get_first_non_explored()
               if root == -1:
                  break
         else:
            dp = self.doDepth(root)
         return dp
      disc = Queue()
      
      return

   def connectivity(self, vx, vy):
      pts = [vx, vy]
      opp = 1
      final = [False]*2
      for v in range(0, 2, 1):
         pathFromP = self.traverse(pts[v], False)
         for i in pathFromP:
            if i == pts[opp-v]:
               final[v] = True
      return final

   def path(self, vx, vy):
      conn = self.connectivity(vx, vy)
      final = [[]]*2
      for r in range(0, 2, 1):
         if conn[r]:

      return final
         


def test():
   G = graph()
   G.addVertex(12)                                    
   G.addEdge(0, 1, False, 1)
   G.addEdge(0, 2, True, 1)
   G.addEdge(0, 3, False, 1)
   G.addEdge(1, 4, True, 1)
   G.addEdge(2, 5, False, 1)
   G.addEdge(3, 6, True, 1)
   G.addEdge(4, 8, False, 1)
   G.addEdge(5, 9, False, 1)
   G.addEdge(6, 10, True, 1)
   G.addEdge(10, 11, False, 1)
   print(G.traverse(None, False))
   G2 = graph()
   G2.addVertex(6)
   G2.addEdge(0, 1, True, 7)
   G2.addEdge(0, 2, True, 9)
   G2.addEdge(0, 5, True, 14)
   G2.addEdge(1, 3, True, 15)
   G2.addEdge(1, 2, True, 10)
   G2.addEdge(2, 3, True, 11)
   G2.addEdge(2, 5, True, 2)
   G2.addEdge(5, 4, True, 9)
   G2.addEdge(3, 4, True, 6)
   print(G2.traverse(None, False))
   print("\n------------\n")
   x=graph()
   x.addVertex(1)
   x.addVertex(1)
   x.addVertex(1)
   x.addVertex(1)
   x.addVertex(1)
   x.addEdge(0,1,False,1)
   x.addEdge(0,2,False,1)
   x.addEdge(0,3,False,1)
   x.addEdge(1,2,False,2)
   x.addEdge(1,4,False,2)
   x.addEdge(2,3,True,3)
   x.addEdge(3,4,True,4)
   x.addEdge(4,5,True,5)
   print(x.traverse(0,False))
   # print("Breadth")
   # print(x.traverse(0,True))
   # print("Breadth; start=None")
   # print(x.traverse(None,True))
   return True

test()