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
        elif self.children == []:
            return
        else:
            for l in self.children:
                if l == leaf.parent:
                    l.children += [leaf]
                    return
                else:
                    l.addChild(leaf)
