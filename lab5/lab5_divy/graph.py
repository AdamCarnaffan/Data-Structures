class Queue:

   def __init__(self):
      self.store = []
   
   def add(self, data):
      self.store += [data]
      return True
   
   def take(self):
      data = self.store[0]
      self.store = self.store[1:]
      return data

   def is_empty(self):
      return len(self.store) == 0

class Stack:

   def __init__(self):
      self.store = []
   
   def add(self, data):
      self.store += [data]
      return True
   
   def take(self):
      data = self.store[-1]
      self.store = self.store[:-1]
      return data
   
   def is_empty(self):
      return len(self.store) == 0
  # generalized methods to add, take, and is_empty to use the adts more interchangably

class graph:

   def __init__(self):
      self.store = []  # adjacency list
      # store = [v1 v2 ...], where each vi is a vertex
      # vi = [c1 c2 ...], where each ci is an adjacent vertex-connection
      # ci = [connection_to, weight]

   def addVertex(self, n): 
      if n <= 0:
         return -1
      for i in range(0, n, 1):  # add n new index slots
         self.store += [[]]
      return len(self.store)
    
   def addEdge(self, from_i, to_i, directed, weight):
      if min(from_i, to_i) < 0 or max(from_i, to_i) > len(self.store) - 1 or weight == 0:
         return False
      exists_flag = False
      for i in range(0, len(self.store[from_i]), 1):  # search the from_i to see if it's already connected to to_i
         if self.store[from_i][i][0] == to_i:  # toggle the flag if connection exists
            exists_flag = True
            break
      if not exists_flag:
         self.store[from_i] += [[to_i, weight]]  # add connection if it didn't exist
      if directed:  # call function again to ensure direction is both ways
         self.addEdge(to_i, from_i, False, weight)
      return True

   def traverse(self, start, typeBreadth):
      if start == None:  # needed because error is thrown otherwise, None cannot be compared with integers
         check = [i for i in range(0, len(self.store) , 1)]
      elif start >= 0:  # start should be within {0 ... n}
         check = [start]
      else:
         return []
      T = []
      if typeBreadth == True:  # breadth traverse
         adt = Queue()
      elif typeBreadth == False:  # depth traverse
         adt = Stack()
      P, D, T, Tcnt = [], [], [], -1
      for i in range(0, len(self.store), 1):  # fill non-visitied/not-processed vertices
         P += [False]
         D += [False]
      for i in check:  # from a specific vertex, or whole tree
         if D[i] == False:  # not visited
            adt.add(i)
            D[i] = True
            if start == None:  # need sublists for None
               T += [[]]
               Tcnt += 1
         while not adt.is_empty():  # there exist vertices to process
            node = adt.take()
            if P[node] == True:  # node has already been processed
               continue
            if start == None:  # lists of lists if None, lese just a singlular list
               T[Tcnt] += [node]
            else:
               T += [node]
            P[node] = True
            for j in range(0, len(self.store[node]), 1):  # checking connections
               if D[self.store[node][j][0]] == False:  # ensure connections are not a repeat
                  adt.add(self.store[node][j][0])
                  D[self.store[node][j][0]] = True
      return T

   def connectivity(self, i1, i2):  # check if connection exists between two paths 
      Element = [False, False]
      path = self.path()  # calling self.path return either [] or a path
      if path[0] != []: # if a path is returned, set to True, else remain False
         Element[0] = True
      if path[1] != []:
         Element[1] = True
      return Element

   def path(self, v1, v2):  
      Element = [[], []]  # worst case return if no paths exist
      Element[0] = self.helper_path(v1, v2)  # check if v1 -> v2 is a path
      Element[1] = self.helper_path(v2, v1)  # check if there is a which path goes other way as well
      return Element

   def helper_path(self, v1, v2):  # I modified Dijkstra's Algorithm to find (ideally a short) path
      if min(v1, v2) < 0 or max(v1, v2) > len(self.store) - 1:
         return []
      values, visited, path_found = [], [], False
      q = Queue()
      q.add(v1)
      for i in range(0, len(self.store), 1):
         values += [[-1, []]] # each values index: [value, [path from v1]]
         visited += [False]
      values[v1][0] = 0
      values[v1][1] += [v1]
      while not q.is_empty():
         vertex = q.take()  # pop a vertex/previous connection to be processed
         if visited[vertex] == True or vertex == v2:  # never reprocess a node and never process the v2 node
            continue
         visited[vertex] = True  # avoid reprocessing
         for i in range(0, len(self.store[vertex]), 1):
            connection = self.store[vertex][i]  # a connection of current vertex being processed
            if visited[connection[0]] == True:  # avoid reprocessing in the case of undirected path
               continue
            pnpv = values[vertex][0] + connection[1]  # potential_new_path_value
            if values[connection[0]][0] == -1:  # never reached vertex, hence -1
               values[connection[0]][0] = pnpv  # set new path value
               values[connection[0]][1] = values[vertex][1][:] + [connection[0]]  # copy the existing path and add the new connection
            elif min(values[connection[0]][0], pnpv) == pnpv and pnpv != values[connection[0]][0]:  # new path is better than existing
               values[connection[0]][0] = pnpv
               values[connection[0]][1] = values[vertex][1][:] + [connection[0]]
            q.add(connection[0])  # add the connection to eventually be processed
      return values[v2][1]

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
   #print(G.traverse(None, False))
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
   print(G2.path(0, 4))
   print("\n------------\n")
   x=graph()
   x.addVertex(1)
   x.addVertex(1)
   x.addVertex(1)
   x.addVertex(1)
   x.addVertex(1)
   print(x.store)
   x.addEdge(0,1,False,1)
   x.addEdge(0,2,False,1)
   x.addEdge(0,3,False,1)
   x.addEdge(1,2,False,2)
   x.addEdge(1,4,False,2)
   x.addEdge(2,3,True,3)
   x.addEdge(3,4,True,4)
   x.addEdge(4,5,True,5)
   print(x.store)
   print("Dpeth")
   print(x.traverse(0,False))
   print("Breadth")
   print(x.traverse(0,True))
   print("Breadth; start=None")
   print(x.traverse(None,True))
   return True

test()