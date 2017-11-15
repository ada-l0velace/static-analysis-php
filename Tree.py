from statements import ProgramStm

class Tree:
    def __init__(self, json):
        self.root = ProgramStm(json)

    def find_all_kind(self,kind):
        a = []
        for child in self.root.children:
            if child.kind == kind:
                a.append(child)
        return a

    def find_all_sinks(self,node, res):
        if hasattr(node, 'kind'):
            if node.kind == 'call':
                res += [node]
        if hasattr(node, 'children'):
            for child in self.root.children:
                self.find_all_sinks(child, res)
        elif hasattr(node, 'left') and hasattr(node, 'right'):
            self.find_all_sinks(node.left, res)
            self.find_all_sinks(node.right, res)
        return res
        
    # def insertLeaf(self, leaf):
    #     if self.root == None:
    #         self.root = leaf
    #     elif self.root == leaf.parent:
    #         self.root.children += [leaf]
    #     else:
    #         unexplored = self.root.children
    #         while unexplored != []:
    #             if unexplored[0] == leaf.parent:
    #                 unexplored[0].children += [leaf]
    #                 return
    #             else:
    #                 unexplored = unexplored[1:] + unexplored[0].children

    # def removeLeaf(self, leaf):
    #     unexplored = self.root.children
    #     while unexplored != []:
    #         if leaf == unexplored[0]:
    #             unexplored[0].parent.children.remove(leaf)
    #         else:
    #             unexplored = unexplored[1:] + unexplored[0].children


    
    
# class Leaf:

#     def __init__(self, value, parent=None):
#         self.parent = parent
#         self.node = node

#     def __eq__(self, other):
#         if other == None:
#             return False
#         return self.value == other.value

