from statements import *
from expressions import *
from pattern import *

class Tree:
    def __init__(self, json):
        self.root = ProgramStm(json)
        self.code_lines = []
        for child in self.root.children:
            self.code_lines.append(str(child))

    def find_all_kind(self,kind):
        a = []
        for child in self.root.children:
            if child.kind == kind:
                a.append(child)
        return a

    def visit(self,node, pattern, line):
        #print 'puts'
        if type(node) == ProgramStm:
            #print node.__dict__
            for child in node.children:
                line += 1
                self.visit(child, pattern, line)
                
        elif type(node) == AssignStm:
            #print 'ASSIGNS'
            node.right.tainted = False
            #print 'BEFORE ASSIGNS',node.right.tainted,node.right
            self.visit(node.right, pattern, line)
            #print 'AFTER ASSIGNS',node.right.tainted,node.right
            #print node.right,line
            node.left.tainted = node.right.tainted
            node.left.flow_list = node.right.flow_list
            self.visit(node.left, pattern, line)
            #print node.left.tainted,node.left
            #print node.left,node.left.tainted

        elif(type(node) == BinaryOperatorExp):
            self.visit(node.right, pattern, line)
            node.left.tainted = node.right.tainted
            self.visit(node.left, pattern, line)
            if node.right.tainted or node.left.tainted:
                node.tainted = True
                #item = FlowItem()
                #node.flow_list += [item]
                node.left.flow_list = node.right.flow_list 

        elif(type(node) == ParenthesisOperatorExp):
            self.visit(node.inner, pattern, line)
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
                item.line = line
                node.flow_list += [item]
                #pattern.set_taintness(node.name, node.tainted)
                #pattern.set_var_flow(node.name, node.flow_list)

        elif(type(node) == EncapsedExp):
            #print 'ENCAPSED'
            c = 0
            for v in node.values:
                self.visit(v, pattern, line)
                if v.tainted:
                    c += 1
                    node.tainted = v.tainted
                #print v.flow_list, 'lol'
                node.flow_list += v.flow_list
            if c == 0:
                node.tainted = False
            #pattern.set_var_flow(node.kind, node.flow_list)
            #print v
        elif(type(node) == IfStm):
            line += 1
            for child in node.body.children:
                line += 1
                self.code_lines.append(str(child))
                self.visit(child, pattern, line)
            if node.alternate:
                line += 1
                self.visit(node.alternate, pattern, line)
        
        elif(type(node) == BlockStm):
            for child in node.children:
                self.code_lines.append(str(child))
                line += 1
                self.visit(child, pattern, line)
        elif(type(node) == WhileStm):
            for child in node.body.children:
                line += 1
                self.visit(child, pattern, line+1)

        elif type(node) == CallExp or issubclass(type(node),SysStm):
            #print node
            #print 'CALLLS'
            flow_list = []
            for param in node.arguments:
                self.visit(param, pattern, line)
                #print param.flow_list, param.name
                if param.tainted:
                    node.tainted = True
                flow_list += param.flow_list
            node.flow_list = flow_list
            if pattern.is_sanitization(node.name):
                node.tainted = False
                pattern.set_taintness(node.name, False)
                item = FlowItem()
                item.name = node.name
                item.line = line
                item.type = FlowItem.SANITIZATION_TYPE
                node.flow_list += [item]

            #print node.name, node.tainted,pattern.is_sanitization(node.name), pattern.sanitizations
            
            if pattern.is_sink(node.name):
                item = FlowItem()
                item.name = node.name
                item.type = FlowItem.SINK_TYPE
                item.line = line
                flow_list.append(item)
                #print node.tainted

                node.flow_list = flow_list
                pattern.set_var_flow(node.name, node.flow_list)
                #print node.tainted

                FAIL = '\033[91m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                ENDC = '\033[0m'
                #print line
                if node.tainted:
                    print WARNING+"Warning: Tainted input reached sink."+ENDC
                    print FAIL+"%s vulnerability found in %s" % (pattern.name, str(self.code_lines[line-2])) + ENDC
                    #print pattern.flows
                else:
                    print line-2
                    print OKGREEN+"No %s vulnerabilities found in %s" % (pattern.name, str(self.code_lines[line-2])) + ENDC
                #for key in flows.keys():

                #print_flow_list(flow_list, self.code_lines)

                
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

