from statements import *
from expressions import *
from pattern import *

class Tree:
    def __init__(self, json):
        self.root = ProgramStm(json)
        self.over = False
        self.code_lines = []
        self.code_lines_cal(self.root)
        #exit(0)
        #print self.code_lines
        #self.code_lines[::-1]

    def find_all_kind(self,kind):
        a = []
        for child in self.root.children:
            if child.kind == kind:
                a.append(child)
        return a

    def code_lines_cal(self, node):
        if node:
            if type(node) == ProgramStm:
                #print node.__dict__
                for child in node.children:
                    for i in range(child.line_start, child.line_end+1):
                        self.code_lines.append(str(child))
                    self.code_lines_cal(child)
            if type(node) == IfStm:
                self.code_lines.append(node.alternate)
                self.code_lines_cal(node.alternate)


        #elif(type(node) == IfStm):

            #print self.code_lines, node.test.line_start, node.test.line_end, 'QLWOWDOQWL'
            #for i in range(node.test.line_start, node.test.line_end+1):
                #print i
                #self.code_lines.append(str(node.test))
            #for child in node.body.children:
                #for i in range(child.line_start, child.line_end+1):
                #    self.code_lines.append(str(child))
                #self.code_lines_cal(child)
            #if node.alternate:
            #    self.code_lines_cal(node.alternate)        
        #elif(type(node) == BlockStm):
        #    for child in node.children:
                #for i in range(child.line_start, child.line_end+1):
                #    self.code_lines.append(str(child))
        #        self.code_lines_cal(child)

        #elif(type(node) == WhileStm):
        #    for child in node.body.children:
        #        for i in range(child.line_start, child.line_end+1):
        #            self.code_lines.append(str(child))
        #        self.code_lines_cal(child)


    def visit(self,node, pattern, line):
        #print 'puts'
        if self.over == True:
            return
        if type(node) == ProgramStm:
            #print node.__dict__
            for child in node.children:
                line += 1
                self.visit(child, pattern, line)
                
        elif type(node) == AssignStm:
            #print 'ASSIGNS'
            node.right.tainted = False
            #print 'BEFORE ASSIGNS',node.right.tainted,node.right
            #print node.right, line
            self.visit(node.right, pattern, line)
            #print 'AFTER ASSIGNS',node.right.tainted,node.right
            #print node.right,line
            node.left.tainted = node.right.tainted
            node.left.flow_list = node.right.flow_list
            node.left.value = node.right.get_value()
            pattern.set_value(node.left.name, node.left.get_value())
            self.visit(node.left, pattern, line)
            #print node.left.tainted,node.left
            #print node.left,node.left.tainted

        elif(type(node) == BinaryOperatorExp):

            self.visit(node.right, pattern, line)
            
            node.left.tainted = node.right.tainted
            self.visit(node.left, pattern, line)
            if node.right.tainted or node.left.tainted:
                node.tainted = True
                node.left.flow_list = node.right.flow_list 
        elif(type(node) == ParenthesisOperatorExp):
            self.visit(node.inner, pattern, line)
            node.tainted = node.inner.tainted
            node.flow_list = node.inner.flow_list
        
        elif(type(node) == VariableExp):
            if not pattern.vars.has_key(node.name):
                print node.flow_list
                pattern.set_taintness(node.name, node.tainted)
                pattern.set_var_flow(node.name, node.flow_list)
            else:
                node.tainted = pattern.get_var_taintness(node.name)
                node.flow_list = pattern.get_var_flow(node.name)
            if not pattern.values.has_key(node.name):
                pattern.set_value(node.name, node.get_value())
            else:
                node.value = pattern.get_value(node.name)

        elif(type(node) == PostOperatorExp):
            self.visit(node.what, pattern, line)
            pattern.set_value(node.what.name, node.what.get_value())
            
                
        elif(type(node) == OffsetlookupExp):
            #print 'OFFSET'
            if pattern.is_input(node.name):
                #print 'wwww'
                node.tainted = True
                item = FlowItem()
                item.name = '$'+node.name+'[\''+node.offset+'\']'
                item.type = FlowItem.INPUT_TYPE 
                item.line = node.line_start
                node.flow_list = [item]
                pattern.set_taintness(node.name, node.tainted)
                pattern.set_var_flow(node.name, node.flow_list)
            else:
                node.tainted = pattern.get_var_taintness(node.name)
                node.flow_list = pattern.get_var_flow(node.name)
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
            #else:
            if len(node.flow_list) > 0:
                node.flow_list[0].line = node.line_start

            #pattern.set_var_flow(node.kind, node.flow_list)
            #print v
        elif(type(node) == IfStm):
            self.visit(node.test, pattern, line)
            if node.is_valid():
                line += 1
                for child in node.body.children:
                    line += 1
                    #self.code_lines.append(str(child))
                    self.visit(child, pattern, line)
            else:
                if node.alternate:
                    line += 1
                    self.visit(node.alternate, pattern, line)        
                    
                
        elif(type(node) == BlockStm):
            for child in node.children:
                #self.code_lines.append(str(child))
                line += 1
                self.visit(child, pattern, line)


        elif(type(node) == WhileStm):
            self.visit(node.test, pattern, line)
            if type(node.test) == BinaryOperatorExp:
                var = node.test.left
            else:
                var = node.test.get_value()
            if node.is_valid():
                for child in node.body.children:
                    line += 1
                    self.visit(child, pattern, line+1)
                if node.is_infinite(var):
                    print "Entered an infinite loop"
                    self.over = True

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
                item.line = node.line_start
                item.type = FlowItem.SANITIZATION_TYPE
                node.flow_list += [item]

            #print node.name, node.tainted,pattern.is_sanitization(node.name), pattern.sanitizations
            
            if pattern.is_sink(node.name):
                item = FlowItem()
                item.name = node.name
                item.type = FlowItem.SINK_TYPE
                item.line = node.line_start
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
                print len(self.code_lines)
                if node.tainted:
                    print WARNING+"Warning: Tainted input reached sink."+ENDC
                    print self.code_lines, node.line_start, node.line_end
                    print FAIL+"%s vulnerability found in %s" % (pattern.name, str(self.code_lines[node.line_start])) + ENDC
                    #print pattern.flows
                else:
                    print self.code_lines
                    print OKGREEN+"No %s vulnerabilities found in %s" % (pattern.name, str(self.code_lines[node.line_start])) + ENDC
                print print_flow_list(flow_list, self.code_lines)
