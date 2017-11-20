from node import Node
from fabric.fabric_all import *
import inspect

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

        #self.name = self.what['name']
    
    def __repr__(self):
        return repr('$'+self.name)+ '['+repr(self.offset)+']'

class VariableExp(Exp):
    """docstring for VariableExp"""
    def __init__(self, json, parent):
        super(VariableExp, self).__init__(json,parent)
        self.name = json["name"]
    def __repr__(self):
        return '$'+self.name

class EncapsedExp(Exp):
    """docstring for EncapsedExp"""
    def __init__(self, json, parent):
        super(EncapsedExp, self).__init__(json,parent)
        self.values = []
        #print json
        for a in json["value"]:
            self.values += [FactoryProducer.get_factory(a['kind'], a, self)]
    def __repr__(self):
        return self.kind

class CallExp(Exp):
    def __init__(self, json, parent):
        super(CallExp, self).__init__(json,parent)
        self.arguments = []
        self.name = json['what']['name']
        #self.name = self.what['name']
        for a in json["arguments"]:
            self.arguments += [FactoryProducer.get_factory(a['kind'], a, self)]
    def __repr__(self):
        return self.name
                
#### OPERATORS
        
class BinaryOperatorExp(Exp):
    """docstring for BinaryOperator"""
    def __init__(self, json, parent):
        super(BinaryOperatorExp, self).__init__(json,parent)
        self.left = FactoryProducer.get_factory(json["left"]["kind"], json["left"], self) 
        self.right = FactoryProducer.get_factory(json["right"]["kind"], json["right"], self) 
    def __repr__(self):
        return self.type

class ParenthesisOperatorExp(Exp):
    """docstring for BinaryOperator"""
    def __init__(self, json, parent):
        super(BinaryOperatorExp, self).__init__(json,parent)
        self.inner = FactoryProducer.get_factory(a['inner']['kind'], a, self)
    def __repr__(self):
        return self.type


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

