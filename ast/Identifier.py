from Node import Node

class Identifier(Node):
    
    ''' Extends Node

       Defines an identifier node

       Properties
       
       name string
       resolution string
    '''
    
    def __init__(self, kind, name, resolution):
        super().__init__(kind)
        self.name = name 
        self.resolution = resolution