from node import Node
from expressions import *
from fabric.fabric_expression import *

class Stm(Node):
    def __init__(self, json, parent):
        super(Stm, self).__init__(json, parent)

class BlockStm(Stm):
    def __init__(self, json, parent=None):
        super(BlockStm, self).__init__(json, parent)
        self.children = []
        for val in json["children"]:
            self.children += [Node(val)] #TODO

class ClassStm(Stm):
    def __init__(self, json, parent):
        super(ClassStm, self).__init__(json, parent)
        self.extends = Node(json["Extends"]) #TODO
        self.implements = Node(json["Implements"])
        self.body = []
        for d in json["body"]:
            self.body += [Stm(d)]

class ParameterStm(Stm):
    def __init__(self, json, parent):
        super(Parameter, self).__init__(json, parent)
        if json["type"] != None:
            self.type = Node(json["type"])

            
class FunctionStm(BlockStm):
    def __init__(self, json, parent):
        super(Function, self).__init__(parent,json)
        self.arguments = []
        for i in json["parameter"]:
            self.arguments += Node(i)
        
class AssignStm(Stm):
    def __init__(self, json, parent):
        super(AssignStm, self).__init__(json, parent)
        self.left = ExpressionFactoryProducer.get_factory(json["left"]["kind"], json["left"]) 
        self.right = ExpressionFactoryProducer.get_factory(json["right"]["kind"], json["right"]) 

