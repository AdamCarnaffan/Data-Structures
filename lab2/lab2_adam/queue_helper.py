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