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

   def sim_path(self, vx, vy):
      if vx == vy:
         return True
      orig = list(self.explored)
      self.explored = self.explored + [vx]
      res = False
      for v in self.adj[vx]:
         if v[0] == vy:
            res = True
            break
         elif v[0] in self.explored:
            continue
         elif (self.sim_path(v[0], vy)):
            res = True
            break
      self.explored = orig
      return res

   def path(self, vx, vy):
      conn = self.connectivity(vx, vy)
      final = [[]]*2
      vals = [vx, vy]
      for r in range(0, 2, 1):
         pt = vals[r]
         if conn[r]:
            self.explored = [pt]
            final[r] = [pt]
            while pt != vals[1-r]:
               for v in self.adj[pt]:
                  if v[0] in self.explored:
                     continue
                  if self.sim_path(v[0], vals[1-r]):
                     self.explored = self.explored + [pt]
                     pt = v[0]
                     final[r] = final[r] + [pt]
                     break
      return final

def main():
   g2 = graph()
   g2.addVertex(10)
   g2.addEdge(0, 1, True, 2)
   g2.addEdge(0, 2, True, 3)
   g2.addEdge(1, 3, True, 2)
   g2.addEdge(2, 3, True, 2)
   g2.addEdge(3, 4, False, 2)
   g2.addEdge(4, 5, True, 2)
   g2.addEdge(4, 6, False, 3)
   g2.addEdge(6, 8, True, 3)
   g2.addEdge(6, 7, True, 5)
   g2.addEdge(7, 9, True, 4)
   g2.addEdge(8, 9, True, 5)
   g2.addEdge(7, 8, False, 1)
   g2.addEdge(9, 6, True, 1)
   g2.addEdge(9, 0, True, 2)
   print("FORE GRAPH 2:")
   print("PATH FROM 0 -> 9 AND 9 -> 0:")
   print(g2.path(0, 9))
   print("ANSWER: [[0, 1, 3, 4, 6, 8, 9], [9, 0]] ")
   print("-------")
   print("Traversal by BREADTH from 0:")
   print(g2.traverse(0, True))
   print("ANSWER: [0, 2, 3, 4, 6, 7, 9, 8, 5, 1] ")
   print("-------")
   print("Traversal by DEPTH from 0")
   print(g2.traverse(0, False))
   print("ANSWER: [0, 2, 3, 4, 6, 7, 9, 8, 5, 1] ")
   print("-------")
   print("None by Breadth:")
   print(g2.traverse(None, True))
   print("None by Depth:")
   print(g2.traverse(None, False))
   print("None Breadth and Depth should both appear the \nsame as starting at 0 except list inside of a list.")
<<<<<<< HEAD
   return

test()
=======

main()
>>>>>>> 671a3ebf2963b4818347d796f1cc78ed215451fc
