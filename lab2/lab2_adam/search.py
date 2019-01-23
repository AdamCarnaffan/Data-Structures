from queue_helper import Queue

class binary_tree:
    def __init__(self, val):
        self.store = [val, [], []]
    
    def display(self, indent=0):
      ind = ''
      for i in range(0, indent, 1):
         ind = ind + '   '
      print(ind + str(self.store[0]))
      if self.store[2] != []:
         self.store[2].display(indent+1)
      if self.store[1] != []:
         self.store[1].display(indent+1)
      return True

    def get_in_order(self):
        final = [self.store[0]]
        if self.store[1] != []:
            final = self.store[1].get_in_order() + final
        if self.store[2] != []:
            final = final + self.store[2].get_in_order()
        return final

    def get_pre_order(self):
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

    def get_post_order(self):
        # opposite traversal of pre order
        return True

    def add_value(self, value):
        if value == self.store[0]:
            return False
        if value > self.store[0]:
            targ = 2
        else:
            targ = 1
        if self.store[targ] == []:
            self.store[targ] = binary_tree(value)
            return True
        else:
            return self.store[targ].add_value(value)

def main():
    x = binary_tree(5)
    x.add_value(4)
    x.add_value(6)
    x.add_value(3)
    x.add_value(4)
    x.display()
    print(x.get_pre_order())
    return True

main()