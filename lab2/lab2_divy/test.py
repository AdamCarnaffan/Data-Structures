import binary_tree
import tree


def test1():
    x = tree.tree(1000)
    y = tree.tree(2000)
    z = tree.tree(3000)
    c = tree.tree(4000)
    d = tree.tree(5000)
    e = tree.tree(6000)
    f = tree.tree(7000)
    g = tree.tree(8000)
    x.AddSuccessor(y)
    x.AddSuccessor(z)
    y.AddSuccessor(c)
    y.AddSuccessor(d)
    z.AddSuccessor(e)
    z.AddSuccessor(f)
    z.AddSuccessor(g)
    x.Print_DepthFirst()
    print("\nBinary Tree Conversion:")
    btree = x.ConvertToBinaryTree()
    btree.display()
    print("\n After Conversion:")
    x.Print_DepthFirst()
    return True

def test2():
    a = binary_tree.binary_tree(1000)
    b = binary_tree.binary_tree(2000)
    c = binary_tree.binary_tree(3000)
    d = binary_tree.binary_tree(4000)
    e = binary_tree.binary_tree(5000)
    f = binary_tree.binary_tree(6000)
    g = binary_tree.binary_tree(7000)
    h = binary_tree.binary_tree(8000)
    a.AddLeft(b)
    b.AddRight(d)
    b.AddLeft(c)
    d.AddRight(e)
    c.AddLeft(f)
    f.AddRight(g)
    g.AddRight(h)
    a.display()
    print(a.Get_LevelOrder())
    return True
test1()
test2()