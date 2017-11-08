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
