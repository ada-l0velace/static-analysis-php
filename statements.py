from node import Node
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
            self.children += [FactoryProducer.get_factory(val["kind"],val, self)] #TODO

            
class AssignStm(Stm):
    def __init__(self, json, parent):
        super(AssignStm, self).__init__(json, parent)
        #print json["right"]['kind']
        self.left = FactoryProducer.get_factory(json["left"]["kind"], json["left"], self) 
        self.right = FactoryProducer.get_factory(json["right"]["kind"], json["right"], self) 

class ProgramStm(BlockStm):
    def __init__(self, json, parent=None):
        super(ProgramStm, self).__init__(json, parent)
