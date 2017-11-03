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

    def getParent(self):
        return self.parent

    def setParent(self, Leaf):
        self.parent = Leaf

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = children

    def addChild(self, child):
        self.children += [child]

    def getChild(self, index):
        return self.children[index]
