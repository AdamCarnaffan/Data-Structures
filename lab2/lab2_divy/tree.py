class tree:
   def __init__(self, x):
      self.store = [x, []]

   def AddSuccessor(self, x):
      self.store[1] = self.store[1] + [x]
      return True
   
   def Print_DepthFirst(self):  # assignment 1
      indent_level = Stack()
      indent_level.push("")
      printer = Stack()
      printer.push(self.store)
      while printer.length() > 0:
         popped = printer.pop()
         indent = indent_level.pop()
         print(indent + str(popped[0]))
         for i in popped[1][::-1]:
            printer.push(i.store)
            indent_level.push(indent + "   ")
      return True

   def Get_LevelOrder(self):  # assignment 2
      order = []
      helper = Queue()
      helper.add(self.store)
      while helper.length() > 0:
         level = helper.take()
         order += [level[0]]
         for i in level[1]:
            helper.add(i.store)
      return order
   
   def ConvertToBinaryTree(self):  # assignment 4
      pass
   



class Stack:  # helper class for assignment 1

   def __init__(self):
      self.data = []
   
   def push(self, new_data):
      self.data += [new_data]
      return True
   
   def pop(self):
      if self.data == []:
         return False
      popped = self.data[len(self.data) - 1]
      self.data = self.data[0:len(self.data) - 1]
      return popped
   
   def length(self):
      return len(self.data)

   def peek(self):
      print(self.data)
      return True


class Queue:  # helper class for assignment 2

   def __init__(self):
      self.data = []
   
   def add(self, new_data):
      self.data += [new_data]
      return True
   
   def take(self):
      if self.data == []:
         return False
      first = self.data[0]
      self.data = self.data[1:len(self.data )]
      return first

   def length(self):
      return len(self.data)

   def peek(self):
      print(self.data)
      return True