from Node import Node

class Identifier(Node):
    
    '''Extends Node

       Defines an identifier node

       Properties
       
       name string
       resolution string
    '''
    
    def __init__(self, kind, name, resolution):
        super().__init__(kind)
        self.name = name 
        self.resolution = resolution
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getResolution(self):
        return self.resolution
    
    def setResolution(self, resolution):
        self.resolution = resolution
