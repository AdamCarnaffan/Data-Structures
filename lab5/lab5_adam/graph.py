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

   def length(self):
      return len(self.vals)

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
      else:
         while (root != -1):
            bld = []
            disc = Queue()
            disc.enqueue([root, self.adj[root]])
            self.explored = self.explored + [root]
            while disc.length() > 0:
               curr = disc.dequeue()[1]
               bld = bld + [curr[0]]
               for v in curr[1]:
                  fnd = False
                  for i in self.explored:
                     if i == v[0]:
                        fnd = True
                        break
                  if not fnd:
                     disc.enqueue([v[0], self.adj[v[0]]])
                     self.explored = self.explored + [v[0]]
            if start != None:
               root = -1
               dp = bld
            else:
               root = self.get_first_non_explored()
               dp = dp + [bld]
      return dp

   def connectivity(self, vx, vy):
      pts = [vx, vy]
      final = [False]*2
      for v in range(0, 2, 1):
         pathFromP = self.traverse(pts[v], False)
         for i in pathFromP:
            if i == pts[1-v]:
               final[v] = True
      return final

   def path(self, vx, vy):
      conn = self.connectivity(vx, vy)
      final = [[]]*2
      vals = [vx, vy]
      for r in range(0, 2, 1):
         pt = vals[r]
         if conn[r]:
            final[r] = [pt]
            while pt != vals[1-r]:
               for v in self.adj[pt]:
                  if self.connectivity(v[0], vals[1-r])[0]:
                     final[r] = final[r] + [v[0]]
                     pt = v[0]
      return final