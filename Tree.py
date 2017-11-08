class Tree:
    def __init__(self, root):
        self.root = root

    def insertLeaf(self, leaf):
        self.root.addChild(leaf)


class Leaf:

    def __init__(self, value, parent=None, children=[]):
        self.parent = parent
        self.value = value
        self.children = list(children)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def addChild(self, leaf):
        if self == leaf.parent:
            self.children += [leaf]
        else:
            unexplored = self.children
            while unexplored != []:
                if unexplored[0] == leaf.parent:
                    unexplored[0].children += [leaf]
                    return
                else:
                    unexplored = unexplored[1:] + unexplored[0].children


a = Leaf(2)
b = Leaf(5, a)
c = Leaf(7, a)
d = Leaf(1, a)
e = Leaf(3, a)
f = Leaf(2, a)
g = Leaf(6, a)
h = Leaf(8, a)
i = Leaf(12, b)
j = Leaf(123, b)
l = Leaf(1222, h)
p = Leaf(129, j)
o = Leaf(765, p)
a.addChild(b)
a.addChild(c)
a.addChild(d)
a.addChild(e)
a.addChild(f)
a.addChild(g)
a.addChild(h)
a.addChild(i)
a.addChild(j)
a.addChild(l)
a.addChild(p)
a.addChild(o)

print("Children of a are: " + str(a.children) +
      " and should be [5,7,1,3,2,6,8]")
print("Children of b are: " + str(b.children) + " and should be [12, 123]")
print("Children of h are: " + str(h.children) + " and should be [1222]")
print("Children of j are: " + str(j.children) + " and should be [129]")
print("Children of p are: " + str(p.children) + " and should be [765]")
