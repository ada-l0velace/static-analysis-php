class Tree:
    def __init__(self, root):
        self.root = root

class Node:

    def __init__(self, value, children = []):
        self.value = value
        if children != []:
            self.children = [children]
        else:
            self.children = children

    def __repr__(self):
        return str(self.value)

    def getValue(self):
        return self.value
        
    def setValue(self, value):
        self.value = value
        
    def setChildren(self, children):
        self.children = children

    def addChild(self, child):
        self.children += [child]

    def getChildren(self):
        return self.children

    def getChild(self, index):
        return self.children[index]
