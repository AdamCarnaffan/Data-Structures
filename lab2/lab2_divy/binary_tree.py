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
        if self.store[2] != []:
            return [False, []]
        root = tree.tree(self.store[0])
        branch = root
        order = tree.Queue()
        next_level = tree.Queue()
        current = self
        while True:
            if current.store[1] != []:
                left = current.store[1]
                branch.store[1] += tree.tree(left.store[0])
                temp = tree.Queue()
                temp.enqueue(current.store[1])
                next_level.enqueue(current.store[1])
                break
        return True


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
