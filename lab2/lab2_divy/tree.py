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
      siblings = Queue()
      branch_node = Queue()
      branch_node.enqueue(self)
      root = binary_tree.binary_tree(self.store[0])
      branch = root
      while siblings.length() > 0 or branch_node.length() > 0:
         current = branch_node.dequeue()
         q = Queue()
         q.enqueue(current)
         for i in current.store[1]:
            q.enqueue(i)
         branch_node.enqueue(q)
         if siblings.length() > 0:
            sib = siblings.dequeue()
            branch.AddLeft(binary_tree.binary_tree(sib.store[0]))
            branch = branch.store[2]
            continue
         else:
            


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