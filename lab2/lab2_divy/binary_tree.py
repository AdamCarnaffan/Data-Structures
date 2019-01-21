import tree


class binary_tree:  # assignment 3

    def __init__(self, data):
        self.store = [data, [], []]

    def AddLeft(self, new_tree):
        self.store[1] = new_tree
        return True

    def AddRight(self, new_tree):
        self.store[2] = new_tree
        return True

    def set_data(self, over_ride_data):  # created just incase it was needed
        self.store[0] = over_ride_data
        return True

    def Get_LevelOrder(self):
        order = []
        helper = tree.Queue()
        helper.enqueue(self.store)
        while helper.length() > 0:
            level = helper.dequeue()
            if level == []:
                continue
            order += [level[0]]
            for i in level[1:len(level)]:
                if i != []:
                    helper.enqueue(i.store)
        return order
    
    def ConvertToTree(self):  # assignment 5
        pass

    def length(self):
        return len(self.store)
    
    def display(self):
        printer = tree.Stack()
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