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

print("test 1")   
test1()

