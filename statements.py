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
            self.children += [Node(val, self)] #TODO

            
class FunctionStm(BlockStm):
    def __init__(self, json, parent):
        super(Function, self).__init__(json, parent)
        self.arguments = []
        for i in json["parameter"]:
            self.arguments += Node(i)
        
class AssignStm(Stm):
    def __init__(self, json, parent):
        super(AssignStm, self).__init__(json, parent)
        self.left = ExpressionFactoryProducer.get_factory(json["left"]["kind"], json["left"]) 
        self.right = ExpressionFactoryProducer.get_factory(json["right"]["kind"], json["right"]) 

class ProgramStm(BlockStm):
    def __init__(self, json, parent=None):
        super(ProgramStm, self).__init__(json, parent)
