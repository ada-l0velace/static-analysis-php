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
        #print 'puts'
        if type(node) == ProgramStm:
            #print node.__dict__
            for child in node.children:
                self.visit(child, pattern)
        elif type(node) == AssignStm:
            #print 'ASSIGNS'
            node.right.tainted = False
            #print 'BEFORE ASSIGNS',node.right.tainted,node.right
            self.visit(node.right, pattern)
            #print 'AFTER ASSIGNS',node.right.tainted,node.right
            node.left.tainted = node.right.tainted
            node.left.flow_list += node.right.flow_list
            self.visit(node.left, pattern)
            #print node.left.tainted,node.left
            #print node.left,node.left.tainted

        elif(type(node) == BinaryOperatorExp):
            self.visit(node.right, pattern)
            node.left.tainted = node.right.tainted
            self.visit(node.left, pattern)
            if node.right.tainted or node.left.tainted:
                node.tainted = True
                #item = FlowItem()
                #node.flow_list += [item]
                node.left.flow_list += node.right.flow_list 

        elif(type(node) == ParenthesisOperatorExp):
            self.visit(node.inner, pattern)
            node.tainted = node.inner.tainted
            node.flow_list += node.inner.flow_list
        elif(type(node) == VariableExp):
            if not pattern.vars.has_key(node.name):
                pattern.set_taintness(node.name, node.tainted)
                pattern.set_var_flow(node.name, node.flow_list)
            else:
                node.tainted = pattern.get_var_taintness(node.name)
                node.flow_list = pattern.get_var_flow(node.name)
                
        elif(type(node) == OffsetlookupExp):
            #print 'OFFSET'
            if pattern.is_input(node.name):
                #print 'wwww'
                node.tainted = True
                item = FlowItem()
                item.name = '$'+node.name+'[\''+node.offset+'\']'
                item.type = FlowItem.INPUT_TYPE
                node.flow_list += [item]
                #pattern.set_taintness(node.name, node.tainted)
                #pattern.set_var_flow(node.name, node.flow_list)

        elif(type(node) == EncapsedExp):
            #print 'ENCAPSED'
            c = 0
            for v in node.values:
                self.visit(v, pattern)
                if v.tainted:
                    c += 1
                    node.tainted = v.tainted
                node.flow_list += v.flow_list
            if c == 0:
                node.tainted = False
            #pattern.set_var_flow(node.kind, node.flow_list)
            #print v
        elif(type(node) == IfStm):
            for child in node.body.children:
                self.visit(child, pattern)
            if node.alternate:
                self.visit(node.alternate, pattern)

        elif(type(node) == BlockStm):
            for child in node.children:
                self.visit(child, pattern)

        elif(type(node) == WhileStm):
            for child in node.body.children:
                self.visit(child, pattern)

        elif type(node) == CallExp or issubclass(type(node),SysStm):
            #print node
            #print 'CALLLS'
            flow_list = []
            for param in node.arguments:
                self.visit(param, pattern)
                if param.tainted:
                    node.tainted = True
                flow_list += param.flow_list
            node.flow_list += flow_list
            if pattern.is_sanitization(node.name):
                node.tainted = False
                pattern.set_taintness(node.name, False)
                item = FlowItem()
                item.name = node.name
                item.type = FlowItem.SANITIZATION_TYPE
                node.flow_list += [item]
            #print node.name, node.tainted,pattern.is_sanitization(node.name), pattern.sanitizations
            
            if pattern.is_sink(node.name):
                item = FlowItem()
                item.name = node.name
                item.type = FlowItem.SINK_TYPE
                flow_list.append(item)
                #print node.tainted

                node.flow_list = flow_list
                pattern.set_var_flow(node.name, node.flow_list)
                #print node.tainted
                flows = {}
                for flow_key in pattern.flows.keys():
                    for flow in pattern.flows[flow_key]:
                        flag = False
                        if flows.has_key(flow_key):
                            for f in flows[flow_key]:
                                if f.name == flow.name:
                                    flag = True
                                    break
                            if not flag:
                                flows[flow_key] += [flow]
                        else:
                            flows[flow_key] = [flow]
                FAIL = '\033[91m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                ENDC = '\033[0m'
                if node.tainted:

                    print WARNING+"Warning: Tainted input reached sink."+ENDC
                    print FAIL+"%s vulnerability found in %s" % (pattern.name, str(node)) + ENDC
                    #print pattern.flows
                else:
                    print OKGREEN+"No %s vulnerabilities found in %s" % (pattern.name, str(node)) + ENDC
                for key in flows.keys():
                    print print_flow_list(flows[key], key)    
                        

                
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

