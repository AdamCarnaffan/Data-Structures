import random

class conway:
   def __init__(self,numlists,indexper,num):
      self.a = numlists
      self.b = indexper
      self.c = num
      self.store = []
      self.s = ""
      # MAKING THE STORED LIST  
      for i in range(0,self.a,1):
         self.store = self.store + ["placeholder"]
         for ele in range(0,len(self.store),1):
            self.store[ele] = []
            for val in range(0,self.b,1):
               if self.c == "zeros":
                  put = 0
               elif self.c == "ones":
                  put = 1
               elif self.c == "random":
                  put = random.randint(0,1)
               else:
                  break
               self.store[ele] += [put]

   def getDisp(self):
      m = ""
      for inside in self.store:
         for vals in inside:
            if vals == 0:
               m = m + " "
            elif vals == 1:  #make ""
               m = m + "*"   #make *
         m = m + "\n"
      self.s = m
      return self.s

   def printDisp(self):
      print(self.getDisp())
      return True

   def setPos(self,row,col,val):
   #VAL CHECK
      if (row >= 0) and (row < self.a):
         riterow = True
      else:
         riterow = "bad"

      if (col >= 0) and (col < self.b):
         ritecol = True
      else:
         ritecol = "ops"
      if (val == 1) or (val == 0):
         itval = val
      else:
         itval = "skip"

      if (itval != "skip") and (riterow != "bad") and (ritecol != "ops"):
         newrow = list(self.store[row])
         newrow[col] = itval
         self.store[row] = list(newrow)
         return True
      else:
         return False

   def find(self,row,col):      ## made a function to possible help with getNeighbours.
      ro = list(self.store[row])
      val = ro[col]
      return val

   def getNeighbours(self,row,col):
   #ERROR CHECK
      check = True
      if (row < 0) or (row > self.a -1):
         check = False
      if (col < 0) or (col > self.b -1):
         check = False
      somelist = []
      if check == False:
         return []
      elif check == True:
         for newr in range(row-1,row+2,1):
            if newr < 0:
               newr = self.a - 1
            if newr > self.a - 1:
               newr = 0
            for newcl in range(col-1,col+2,1):
               if newcl < 0:
                  newcl = self.b - 1
               if newcl > self.b - 1:
                  newcl = 0
               if (newr == row) and (newcl == col):
                  continue
               add = self.find(newr,newcl)
               somelist = somelist + [add]
      return somelist

   def evolve(self,rule):
      nextstate = []
      for i in range(0,self.a,1):
         nextstate = nextstate + ["placeholder"]
         for ele in range(0,len(nextstate),1):
            nextstate[ele] = []
            for val in range(0,self.b,1):
               nextstate[ele] += [0]

      for row in range(0,self.a,1):
         for col in range(0,self.b,1):
            nays = list(self.getNeighbours(row,col))
            val = self.find(row,col)
            newval = rule(val,nays)
            nextstate[row][col] = newval
      self.store = list(nextstate)
      return True