def sort_lists_by_length(l):
    res = list(l)
    for x in range(0, len(l), 1):
        for y in range(0, len(l), 1):
            if len(res[x]) > len(res[y]):
                temp = res[x]
                res[x] = res[y]
                res[y] = temp
    return res

class tree:
    def __init__(self, x):
        self.store = [x, []]
        
    def AddSuccessor(self, x):
        self.store[1] = self.store[1] + [x]
        return True
        
    def Print_DepthFirst(self):
        disp = ""
        for val in self.store[1]:
            disp = disp + "   " + str(val.store[0])
        print(disp)
        return True
        
    def Get_LevelOrder(self):
        tree = []
        for val in self.store[1]:
            tree = tree + val.Get_LevelOrder()
        if len(tree) < 1:
            return [[self.store[0]]]
        branches = []
        # Get longest
        sorted = sort_lists_by_length(tree)
        for b in range(0, len(sorted[0]), 1):
            branches = branches + [[]]
        for comp in sorted:
            for x in range(0, len(comp), 1):
                branches[x] = branches[x] + [comp[x]]
        print(branches)
        return [[self.store[0]] + branches]

def main():
    a = tree(5)
    b = tree(9)
    e = tree(4)
    a.AddSuccessor(tree(20))
    b.AddSuccessor(e)
    #e.AddSuccessor(tree(12))
    a.AddSuccessor(b)
    #a.Print_DepthFirst()
    print(a.Get_LevelOrder())
    
main()
