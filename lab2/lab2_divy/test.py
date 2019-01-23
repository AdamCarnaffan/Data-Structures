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
    print(x.Get_LevelOrder())
    print("\nBinary Tree Conversion:")
    btree = x.ConvertToBinaryTree()
    btree.display()
    print(btree.Get_LevelOrder())
    print("\nConvert Back:")
    reverted = btree.ConvertToTree()
    reverted.Print_DepthFirst()
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
    a.AddRight(c)
    b.AddRight(d)
    b.AddLeft(e)
    c.AddRight(f)
    c.AddLeft(g)
    g.AddRight(h)
    a.display()
    return True


def test3():
   a = tree.tree("texmf")
   a.AddSuccessor(tree.tree("doc"))
   a.AddSuccessor(tree.tree("fonts"))
   a.AddSuccessor(tree.tree("source"))
   b = tree.tree("tex")
   b.AddSuccessor(tree.tree("generic"))
   b.AddSuccessor(tree.tree("latex"))
   b.AddSuccessor(tree.tree("plain"))
   a.AddSuccessor(b)
   a.AddSuccessor(tree.tree("texdoc"))
   a.Print_DepthFirst()
   x = a.ConvertToBinaryTree()
   x.display()
   l = x.ConvertToTree()
   l.Print_DepthFirst()

print("test 1")   
test1()
print("\ntest 3")
test3()

