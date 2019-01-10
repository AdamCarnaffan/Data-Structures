class Stack:
    
    def __init__(self):
        self.vals = []
        self.length = 0
    
    def push(self, val):
        self.vals = self.vals + [val]
        self.length = self.length + 1
        return True
        
    def pop(self):
        if self.length < 1:
            return False # Not perfect because False could be a valid part of stack
        returnVal = self.vals[len(self.vals)-1]
        self.vals = self.vals[0:len(self.vals)-1]
        self.length = self.length - 1
        return returnVal
