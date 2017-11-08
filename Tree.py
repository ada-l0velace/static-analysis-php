class Tree:
    def __init__(self, root):
        self.root = root

    def insertLeaf(self, leaf):
        if self.root == leaf.parent:
            self.root.children += [leaf]
        else:
            unexplored = self.root.children
            while unexplored != []:
                if unexplored[0] == leaf.parent:
                    unexplored[0].children += [leaf]
                    return
                else:
                    unexplored = unexplored[1:] + unexplored[0].children

    def removeLeaf(self, leaf):
        unexplored = self.root.children
        while unexplored != []:
            if leaf == unexplored[0]:
                unexplored[0].parent.children.remove(leaf)
            else:
                unexplored = unexplored[1:] + unexplored[0].children


class Leaf:

    def __init__(self, value, parent=None, children=[]):
        self.parent = parent
        self.value = value
        self.children = list(children)

    def __eq__(self, other):
        return self.value == other.value
