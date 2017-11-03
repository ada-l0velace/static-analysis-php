from Node import Node

class Doc(Node):
    
    '''Documentation
    
       Extends Node
    
       A comment or documentation
    
       Properties
    
          isDoc Boolean
          lines Array<String>
    '''
    
    def __init__(self, kind, isDoc, lines):
        super().__init__(kind)
        self.isDoc = isDoc
        self.lines = lines