from tree import *

class binary_tree:  # assignment 3

    def __init__(self, data):
        self.store = [data]

    def AddLeft(self, new_tree):
        if self.length() == 1:
            self.store += [new_tree]
        return True

    def AddRight(self, new_tree):
        if self.length() == 1:
            self.store += [[]] + [new_tree]
        elif self.length == 2:
            self.store += [new_tree]
        return True

    def Get_LevelOrder(self):
        order = []
        helper = Queue()
        helper.add(self.store)
        while helper.length() > 0:
            level = helper.take()
            if level == []:
                continue
            order += [level[0]]
            for i in level[1:len(level)]:
                helper.add(i.store)
        return order
    
    def ConvertToTree(self):  # assignment 5
        pass

    def length(self):
        return len(self.store)
