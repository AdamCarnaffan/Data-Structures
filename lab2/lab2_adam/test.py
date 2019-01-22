import binary_tree as bt
import tree as tt


def test3():
   a = tt.tree("texmf")
   a.AddSuccessor(tt.tree("doc"))
   a.AddSuccessor(tt.tree("fonts"))
   a.AddSuccessor(tt.tree("source"))
   b = tt.tree("tex")
   b.AddSuccessor(tt.tree("generic"))
   b.AddSuccessor(tt.tree("latex"))
   b.AddSuccessor(tt.tree("plain"))
   a.AddSuccessor(b)
   a.AddSuccessor(tt.tree("texdoc"))
   #print(a.Get_LevelOrder())
   l = a.ConvertToBinaryTree()
   print(l.Get_LevelOrder())
   l.Get_DepthFirst()
   print(l.store[1].store[2].store[2].store[2].store[1].store[0])

def test1():
    x = tt.tree(1000)
    y = tt.tree(2000)
    z = tt.tree(3000)
    c = tt.tree(4000)
    d = tt.tree(5000)
    e = tt.tree(6000)
    f = tt.tree(7000)
    g = tt.tree(8000)
    x.AddSuccessor(y)
    x.AddSuccessor(z)
    y.AddSuccessor(c)
    y.AddSuccessor(d)
    z.AddSuccessor(e)
    z.AddSuccessor(f)
    z.AddSuccessor(g)
    x.Get_DepthFirst()
    print("\nBinary Tree Conversion:")
    btree = x.ConvertToBinaryTree()
    btree.Get_DepthFirst()
    print("\n After Conversion:")
    x.Get_DepthFirst()
    return True

def test2():
    a = bt.binary_tree(1000)
    b = bt.binary_tree(2000)
    c = bt.binary_tree(3000)
    d = bt.binary_tree(4000)
    e = bt.binary_tree(5000)
    f = bt.binary_tree(6000)
    g = bt.binary_tree(7000)
    h = bt.binary_tree(8000)
    a.AddLeft(b)
    b.AddRight(d)
    b.AddLeft(c)
    d.AddRight(e)
    c.AddLeft(f)
    f.AddRight(g)
    g.AddRight(h)
    a.Get_DepthFirst()
    print(a.Get_LevelOrder())
    return True


test1()
test2()
test3()