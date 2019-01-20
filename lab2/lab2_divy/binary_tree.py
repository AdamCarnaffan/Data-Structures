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
        elif self.length() == 2:
            self.store += [new_tree]
        return True

    def set_data(self, over_ride_data):
        self.store[0] = over_ride_data
        return True

    def Get_LevelOrder(self):
        order = []
        helper = Queue()
        helper.enqueue(self.store)
        while helper.length() > 0:
            level = helper.dequeue()
            if level == []:
                continue
            order += [level[0]]
            for i in level[1:len(level)]:
                helper.enqueue(i.store)
        return order
    
    def ConvertToTree(self):  # assignment 5
        pass

    def length(self):
        return len(self.store)
    
    def display(self):
        printer = Stack()
        printer.push(self.store)
        printer.push("")
        while printer.length() > 0:
            indent = printer.pop()
            node = printer.pop()
            print(indent + str(node[0]))
            node = node[1:len(node)]
            for i in range(len(node) - 1, -1, -1):  # doing reverse order to make the display 'correct'
                if node[i] != []:
                    printer.push(node[i].store)
                    printer.push(indent + "   ")
        return True
