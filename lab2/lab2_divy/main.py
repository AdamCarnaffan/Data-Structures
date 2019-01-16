from tree import tree

def main():
    x = tree(1000)
    y = tree(2000)
    z = tree(3000)
    c = tree(5000)
    d = tree(6000)
    e = tree(7000)
    f = tree(8000)
    g = tree(9000)
    x.AddSuccessor(y)
    x.AddSuccessor(z)
    y.AddSuccessor(c)
    y.AddSuccessor(d)
    z.AddSuccessor(e)
    z.AddSuccessor(f)
    z.AddSuccessor(g)
    x.display()
    print(x.Get_LevelOrder())
    return True

main()