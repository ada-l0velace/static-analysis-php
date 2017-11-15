from Node import Node

class Stm(Node):
    def __init__(self, json, parent):
        super().__init__(parent, json)
        if json:
            self.items = json["items"]

class AssignStm(Stm):
    def __init__(self, json, parent):
        super().__init__(parent, json)
        self.left = Exp(json[left]) #TODO
        self.right = Exp(json[right]) #TODO

class BlockStm(Stm):
    def __init__(self, json, parent=None):
        super().__init__(parent, json)
        self.children = []
        for val in json["children"]:
            self.children += [Node(val)] #TODO

class Class(Stm):
    def __init__(self, json, parent):
        super().__init__(parent, json)
        self.extends = Node(json["Extends"]) #TODO
        self.implements = Node(json["Implements"])
        self.body = []
        for d in json["body"]:
            self.body += [Stm(d)]

class Parameter(Stm):
    def __init__(self, json, parent):
        super().__init__(parent, json)
        if json["type"] != None:
            self.type = Node(json["type"])

            
class Function(Stm):
    def __init(self, json, parent):
        super().__init__(parent,json)
        self.arguments = []
        for i in json["parameter"]:
            self.arguments += Node(i)
