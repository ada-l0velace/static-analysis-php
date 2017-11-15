from node import Node
from fabric.fabric_expression import *
import inspect

class Exp(Node):
    """docstring for Exp"""
    def __init__(self, json=None, parent=None):
        self.parent = parent    
        self.parse_from_json(json)

    def parse_from_json(self, json):
        literal = ['string', 'integer']
        operations = ['bin', 'pre', 'post', 'parenthesis', 'unary', 'cast']
        expressions = ['constref', 'variable', 'offsetlookup', 'call', 'encapsed'] + literal + operations
        for key in json:
            if type(json[key]) == dict and json[key].has_key('kind') and json[key]['kind'] in expressions:
                self.__dict__[key] = ExpressionFactoryProducer.get_factory(json[key]['kind'], json[key],self)
            else:   
                if key not in ['loc', 'byref', 'curly', 'resolution']:
                    self.__dict__[key] = json[key]

class ConsrefExp(Exp):
    """docstring for ConsrefExp"""
    def __init__(self, json, parent):
        super(ConsrefExp, self).__init__(json,parent)

class OffsetlookupExp(Exp):
    """docstring for OffsetlookupExp"""
    def __init__(self, json, parent):
        super(OffsetlookupExp, self).__init__(json,parent)
    
    def __repr__(self):
        return repr(self.what)+ '['+repr(self.offset)+']'

class VariableExp(Exp):
    """docstring for VariableExp"""
    def __init__(self, json, parent):
        super(VariableExp, self).__init__(json,parent)
    def __repr__(self):
        return '$'+self.name
class EncapsedExp(Exp):
    """docstring for EncapsedExp"""
    def __init__(self, json, parent):
        super(EncapsedExp, self).__init__(json,parent)
        self.values = []
        #print json
        for a in json["value"]:
            self.values += [ExpressionFactoryProducer.get_factory(a['kind'], a, self)]
    def __repr__(self):
        return self.kind

class CallExp(Exp):
    def __init__(self, json, parent):
        super(CallExp, self).__init__(json,parent)
        self.arguments = []
        for a in json["arguments"]:
            self.arguments += [ExpressionFactoryProducer.get_factory(a['kind'], a, self)]
    def __repr__(self):
        return self.what['name']
                
#### OPERATORS
        
class BinaryOperatorExp(Exp):
    """docstring for BinaryOperator"""
    def __init__(self, json, parent):
        super(BinaryOperatorExp, self).__init__(json,parent)


#### LITERALS

class StringExp(Exp):
    """docstring for StringExp"""
    def __init__(self, json, parent):
        super(StringExp, self).__init__(json,parent)
    def __repr__(self):
        return self.value


