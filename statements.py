from node import *
from expressions import *
from fabric.fabric_all import *

class Stm(Node):
    def __init__(self, json, parent):
        super(Stm, self).__init__(json, parent)

class BlockStm(Stm):
    def __init__(self, json, parent=None):
        super(BlockStm, self).__init__(json, parent)
        self.children = []
        for val in json["children"]:
            self.children += [FactoryProducer.get_factory(val["kind"],val, self)]

    def is_infinite(self, node):
        for c in self.children:
            if (c.is_infinite(node)) == False:
                return False
        return True

    def __repr__(self):
        return ';\n\t'.join([str(x) for x in self.children]) + ';'
            
            
class AssignStm(Stm):
    def __init__(self, json, parent):
        super(AssignStm, self).__init__(json, parent)
        #print json["right"]['kind']
        self.left = FactoryProducer.get_factory(json["left"]["kind"], json["left"], self) 
        self.right = FactoryProducer.get_factory(json["right"]["kind"], json["right"], self)
        self.left.value = self.right.get_value()
        
    def __repr__(self):
        return str(self.left)+self.operator+str(self.right)

    
    def is_infinite(self, node):
        if self.left.name == node.name:
            return False
        return True

class ProgramStm(BlockStm):
    def __init__(self, json, parent=None):
        super(ProgramStm, self).__init__(json, parent)
        self.errors = []
        for e in json["errors"]:
            self.errors += [FactoryProducer.get_factory(e["kind"],e, self)]

class SysStm(Stm):
    def __init__(self, json, parent=None):
        self.super_constructor(json, parent)
        self.name = json["kind"]
        self.arguments = []
        if "arguments" in json.keys():
            for arguments in json["arguments"]:
                self.arguments += [FactoryProducer.get_factory(arguments["kind"],arguments, self)]
                
    def super_constructor(self, json, parent):
        super(SysStm, self).__init__(json, parent)

    def __repr__(self):
        return self.name + ','.join([x.__str__() for x in self.arguments])

        
class EchoStm(SysStm):
    def __init__(self, json, parent=None):
        super(EchoStm, self).__init__(json, parent)

    def __repr__(self):
        return self.name + '('+ ','.join([str(x) for x in self.arguments]) + ')'

class IfStm(Stm):
    def __init__(self, json, parent=None):
        super(IfStm, self).__init__(json, parent)
        self.test = FactoryProducer.get_factory(json["test"]["kind"], json["test"], self)
        self.body = BlockStm(json["body"], self)
        if json["alternate"] != None:
            self.alternate = FactoryProducer.get_factory(json["alternate"]["kind"], json["alternate"], self)
        else:
            self.alternate = None
            
    def is_valid(self):
        if type(self.test) == BreakNode:
            return False
        if self.test.is_valid():
            return True
        else:
            return False

    def is_infinite(self, node):
        if self.alternate != None:
            return self.body.is_infinite(node) or self.alternate.body.is_infinite(node)
        else:
            return self.body.is_infinite(node)

    def __repr__(self):
        if self.alternate and self.alternate.test:
            else_str = '    else' + str(self.alternate)
        elif self.alternate:
            else_str = '    else {\n\t' + str(self.alternate) + '\n    }'
        else:
            else_str = ''
        return 'if ('+str(self.test)+ ')' + '{\n\t' + str(self.body) + '\n' + else_str
            

class WhileStm(Stm):
    def __init__(self, json, parent=None):
        super(WhileStm, self).__init__(json, parent)
        self.test = FactoryProducer.get_factory(json["test"]["kind"], json["test"], self)
        self.body = BlockStm(json["body"], self)
        
    def is_valid(self):
        return self.test.is_valid()

    def is_infinite(self, node):
        Bexp = ["==", ">=", "<=", "!=", "<", ">"]
        if self.is_valid():
            if type(self.test) == NumberExp:
                if self.test.get_value() == 1:
                    return True
            elif type(self.test) == BinaryOperatorExp and self.test.type in Bexp:
                if self.body.is_infinite(self.test.left):
                    return True
                else:
                    return self.body.is_infinite(node)
    def __repr__(self):
        return 'while('+str(self.test)+ ')' + '{\n\t' + str(self.body) + '\n    }'

        
class PrintStm(SysStm):
    def __init__(self, json, parent=None):
        super(PrintStm, self).super_constructor(json, parent)
        self.name = json["kind"]
        self.arguments = [FactoryProducer.get_factory(json["arguments"]["kind"], json["arguments"], self)]
        
class ExitStm(SysStm):
    def __init__(self, json, parent=None):
        super(ExitStm, self).__init__(json, parent)
        if json["status"] != None:
            self.arguments = [FactoryProducer.get_factory(json["status"]["kind"], json["status"], self)]

    def __repr__(self):
        return self.name +'('+ str(''.join([str(x) for x in self.arguments])) + ')'
