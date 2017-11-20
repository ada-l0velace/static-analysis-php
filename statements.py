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
            self.children += [FactoryProducer.get_factory(val["kind"],val, self)]

            
class AssignStm(Stm):
    def __init__(self, json, parent):
        super(AssignStm, self).__init__(json, parent)
        #print json["right"]['kind']
        self.left = FactoryProducer.get_factory(json["left"]["kind"], json["left"], self) 
        self.right = FactoryProducer.get_factory(json["right"]["kind"], json["right"], self)
    def __repr__(self):
        return self.kind 

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

class WhileStm(Stm):
    def __init__(self, json, parent=None):
        super(WhileStm, self).__init__(json, parent)
        self.test = FactoryProducer.get_factory(json["test"]["kind"], json["test"], self)
        self.body = BlockStm(json["body"], self)
        
class PrintStm(SysStm):
    def __init__(self, json, parent=None):
        super(PrintStm, self).super_constructor(json, parent)
        self.name = json["kind"]
        self.arguments = [FactoryProducer.get_factory(json["arguments"]["kind"], json["arguments"], self)]

class ExitStm(SysStm):
    def __init__(self, json, parent=None):
        super(ExitStm, self).__init__(json, parent)
        if json["status"] != None:
            self.status = FactoryProducer.get_factory(json["status"]["kind"], json["status"], self)
        else:
        	self.status = None

    def __repr__(self):
    	return self.name +'('+ str(self.status) + ')'

