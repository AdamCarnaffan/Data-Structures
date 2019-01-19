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

    def display(self, indent):
        print(''.join(['   ' for i in range(0, indent, 1)]) + self.store[0])
        for t in self.store[1]:
            t.display(indent + 1)
        return True

    def Get_LevelOrder(self, start=True):
        children = []
        for t in self.store[1]:
            children = children + t.Get_LevelOrder(False)
        return [[self.store[0]] + children]

def main():
    a = tree("texmf")
    b = tree("tex")
    e = tree("plain")
    e.AddSuccessor(tree("new"))
    b.AddSuccessor(tree("generic"))
    b.AddSuccessor(tree("latex"))
    b.AddSuccessor(e)
    a.AddSuccessor(tree("doc"))
    a.AddSuccessor(tree("font"))
    a.AddSuccessor(tree("source"))
    a.AddSuccessor(b)
    a.AddSuccessor(tree("texdoc"))
    print(a.Get_LevelOrder())

main()
