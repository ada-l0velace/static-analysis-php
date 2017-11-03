from Node import Node

class Label(Node):
    
    ''' Label

        Extends Node

        A label statement (referenced by goto)

        Properties

           name String
    '''
    def __init__(self, kind, name):
        super().__init__(kind)
        self.name = name