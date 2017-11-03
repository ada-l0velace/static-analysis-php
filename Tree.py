class Tree:
    def __init__(self, root):
        self.root = root

class Leaf:

    def __init__(self, value, parent = None, children = []):
        self.parent = parent
        self.value = value
        if children != []:
            self.children = [children]
        else:
            self.children = children

    def __repr__(self):
        return str(self.value)

    def addChild(self, child):
        self.children += [child]
