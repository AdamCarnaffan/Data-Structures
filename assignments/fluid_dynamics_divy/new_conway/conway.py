import random
from rule import rule

class conway:

   def __init__(self, rows, columns, number_type):
      self.rows = rows
      self.columns = columns
      self.store = self.generate_store(self.rows, self.columns, number_type)

   def generate_store(self, rows, columns, number_type):
      store = []
      for i in range(0, rows, 1):  # create a 2-D array
         store += [[]]
         if number_type == "zeros":
            store[i] += [0 for i in range(0, columns, 1)]
         elif number_type == "random":
            store[i] += [random.randint(0, 1) for i in range(0, columns, 1)]
         else:
            break
      return store

   def getDisp(self):  # generate a display string
      display = ""
      for i in range(0, len(self.store), 1):
         for j in self.store[i]:
            if j == 0:
               display += " "
            elif j == 1:
               display += "*"
         display += "\n"
      return display

   def printDisp(self):  # print the display string
      print(self.getDisp())
      return True

   def setPos(self, row, column, value):  # assign a value to a specific position
      if min(row, column) < 0 or row >= self.rows or column >= self.columns:
         return False
      self.store[row][column] = value
      return True
   
   def getNeighbours(self, row, column):  # generate a list of neighbours
      if min(row, column) < 0 or row >= self.rows or column >= self.columns:
         return False
      neighbours = []  # surrounding points
      for i in range(row - 1, row + 2, 1):
         for j in range(column - 1, column + 2, 1):
            if i == row and j == column:
               continue
            if i < 0:
               i = self.rows - 1
            elif i >= self.rows:
               i = 0
            if j < 0:
               j = self.columns - 1
            elif j >= self.columns:
               j = 0
            neighbours += [self.store[i][j]]
      return neighbours
   
   def evolve(self, function_rule):  # generate next state according to the function-input
      next_state = self.generate_store(self.rows, self.columns, "zeros")
      for i in range(0, self.rows, 1):
         for j in range(0, self.columns, 1):
            next_state[i][j] = function_rule(self.store[i][j], self.getNeighbours(i, j))
      self.store = next_state
      return True


def main():
   cw = conway(5, 5, "random")
   cw.printDisp()
   print(cw.store)
   print(cw.getNeighbours(3, 4))
   cw.evolve(rule)
   print(cw.store)
   return True


main()
         