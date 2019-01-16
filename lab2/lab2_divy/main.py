from tree import tree

def main():
    x=tree(1000)
    y=tree(2000)
    z=tree(3000)
    x.AddSuccessor(y)
    x.AddSuccessor(z)
    c=tree(5000)
    z.AddSuccessor(c)
    x.display()
    return True

main()