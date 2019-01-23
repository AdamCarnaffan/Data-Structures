import binary_tree


class tree:

   def __init__(self, x):
      self.store = [x, []]

   def AddSuccessor(self, x):
      self.store[1] = self.store[1] + [x]
      return True

   def Print_DepthFirst(self):  # assignment 1
      printer = Stack()
      printer.push(self.store)
      printer.push("")
      while printer.length() > 0:
         indent = printer.pop()
         popped = printer.pop()
         print(indent + str(popped[0]))
         for i in range(len(popped[1]) - 1, -1, -1):  # doing reverse order to make the display 'correct'
            printer.push(popped[1][i].store)
            printer.push(indent + "   ")
      return True

   def Get_LevelOrder(self):  # assignment 2
      order = []
      helper = Queue()
      helper.enqueue(self.store)
      while helper.length() > 0:
         level = helper.dequeue()
         order += [level[0]]
         for i in level[1]:
            helper.enqueue(i.store)
      return order
   
   def ConvertToBinaryTree(self):  # assignment 4
      order = Queue()
      next_level = Queue()
      root = binary_tree.binary_tree(self.store[0])
      branch = root
      current = self
      while True:
         if len(current.store[1]) > 0:
            child1 = current.store[1][0]
            branch.AddLeft(binary_tree.binary_tree(child1.store[0]))
            if len(current.store[1]) > 1:
               temp = Queue()
               temp.enqueue(branch.store[1])
               for i in current.store[1]:
                  temp.enqueue(i)
               next_level.enqueue(temp)
         if order.length() > 0:
            next1 = order.dequeue()
            branch.AddRight(binary_tree.binary_tree(next1.store[0]))
            current = next1
            branch = branch.store[2]
            continue
         elif next_level.length() > 0:
            order = next_level.dequeue()
            branch = order.dequeue()
            current = order.dequeue()
         else:
            return root
      return root



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


class Queue:  # helper class for assignment 2 and 3

   def __init__(self):
      self.data = []
   
   def enqueue(self, new_data):
      self.data += [new_data]
      return True
   
   def dequeue(self):
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