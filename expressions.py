from node import Node
from fabric.fabric_all import *
import inspect
from operations import Operations

class Exp(Node):
    """docstring for Exp"""
    def __init__(self, json=None, parent=None):
        super(Exp, self).__init__(json,parent)
        #self.loc = json['loc']
        #self.parent = parent    
        #self.parse_from_json(json)
        
class ConsrefExp(Exp):
    """docstring for ConsrefExp"""
    def __init__(self, json, parent):
        super(ConsrefExp, self).__init__(json,parent)

class OffsetlookupExp(Exp):
    """docstring for OffsetlookupExp"""
    def __init__(self, json, parent):
        super(OffsetlookupExp, self).__init__(json,parent)
        
        self.name = json['what']['name']
        self.offset = json['offset']['value']
        self.value = self.name

        #self.name = self.what['name']
    
    def __repr__(self):
        return repr('$'+self.name)+ '['+repr(self.offset)+']'
    
class VariableExp(Exp):
    """docstring for VariableExp"""
    def __init__(self, json, parent):
        super(VariableExp, self).__init__(json,parent)
        #print json
        self.name = json["name"]
        self.value = ""
    def __repr__(self):
        return '$'+self.name        

class EncapsedExp(Exp):
    """docstring for EncapsedExp"""
    def __init__(self, json, parent):
        super(EncapsedExp, self).__init__(json,parent)
        self.values = []
        self.value = ""
        #print json
        for a in json["value"]:
            self.values += [FactoryProducer.get_factory(a['kind'], a, self)]
        for i in self.values:
            self.value += i.value
            
    def __repr__(self):
        return ''.join([x.__str__() for x in self.values])

class CallExp(Exp):
    def __init__(self, json, parent):
        super(CallExp, self).__init__(json,parent)
        self.arguments = []
        self.name = json['what']['name']
        #self.name = self.what['name']
        for a in json["arguments"]:
            self.arguments += [FactoryProducer.get_factory(a['kind'], a, self)]
        self.value = None
            
    def __repr__(self):
        return self.name + '(' + ','.join([x.__str__() for x in self.arguments]) + ')'
                
#### OPERATORS
        
class BinaryOperatorExp(Exp):
    """docstring for BinaryOperator"""
    def __init__(self, json, parent):
        super(BinaryOperatorExp, self).__init__(json,parent)
        self.left = FactoryProducer.get_factory(json["left"]["kind"], json["left"], self) 
        self.right = FactoryProducer.get_factory(json["right"]["kind"], json["right"], self)
        if self.type in ['+', '-', '*', '.']:
            self.value = Operations.operate(self.type, self.left.value, self.right.value)

    def __repr__(self):
        return self.left.__str__() + self.type + self.right.__str__()

    def is_valid(self):
        if self.type == '==':
            return self.left.value == self.right.value
        elif self.type == '<=':
            return self.left.value <= self.right.value
        elif self.type == '>=':
            return self.left.value >= self.right.value            
        elif self.type == '>':
            return self.left.value >= self.right.value            
        elif self.type == '<':
            return self.left.value >= self.right.value
        
class ParenthesisOperatorExp(Exp):
    """docstring for BinaryOperator"""
    def __init__(self, json, parent):
        super(ParenthesisOperatorExp, self).__init__(json,parent)
        self.name = self.kind
        self.inner = FactoryProducer.get_factory(json['inner']['kind'], json['inner'], self)
    def __repr__(self):
        return '(' + self.inner.__str__() + ')'


#### LITERALS

class StringExp(Exp):
    """docstring for StringExp"""
    def __init__(self, json, parent):
        super(StringExp, self).__init__(json,parent)
    def __repr__(self):
        return '"'+self.value+'"'

class NumberExp(Exp):
    """docstring for NumberExp"""
    def __init__(self, json, parent):
        super(NumberExp, self).__init__(json,parent)
    
    def __repr__(self):
        return self.value
