from statements import *
from expressions import *
from pattern import *

class Tree:
    def __init__(self, json):
        self.root = ProgramStm(json)

    def find_all_kind(self,kind):
        a = []
        for child in self.root.children:
            if child.kind == kind:
                a.append(child)
        return a

    def visit(self,node, pattern):
        if(type(node) == CallExp):
            #print node, node.tainted

            flow_list = []
            for param in node.arguments:
                self.visit(param, pattern)
            
            #t = t or pattern.get_var_taintness(param.name)
            #if param.flow_list:
            flow_list += param.flow_list
            #print t
            #node.tainted = t
            node.flow_list = flow_list
            

            if pattern.is_sanitization(node.name):
                node.tainted = False
                pattern.set_taintness(node.name, False)
                item = FlowItem()
                item.name = node.name
                item.type = FlowItem.SANITIZATION_TYPE
                node.flow_list += [item]
            
            if pattern.is_sink(node.name):
                item = FlowItem()
                item.name = node.name
                item.type = FlowItem.SINK_TYPE
                node.flow_list.append(item)
                #print node.tainted
                if node.tainted:
                    print "Warning: Tainted input reached sink."
                
                node.flow_list = flow_list
        elif type(node) == ProgramStm:
            #print node.__dict__
            for child in node.children:
                self.visit(child, pattern)
        elif type(node) == AssignStm:
            #print node
            self.visit(node.left, pattern)
            self.visit(node.right, pattern)
            
        elif(type(node) == VariableExp):
            #print node,node.tainted
            node.tainted = pattern.get_var_taintness(node.name)
            node.flow_list = pattern.get_var_flow(node.name)
            
        elif(type(node) == OffsetlookupExp):
            if pattern.is_input(node.name):
                node.tainted = True
                item = FlowItem()
                item.name = node.name
                item.type = FlowItem.INPUT_TYPE
                node.flow_list += [item]
                #print '...'
            else:
                node.tainted = pattern.get_var_taintness(node.name)
                node.flow_list = pattern.get_var_flow(node.name)

        elif(type(node) == EncapsedExp):
            #print node
            for v in node.values:
                self.visit(v, pattern)
                #print v
            
            node.tainted = False
        
                #print flow_list
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

