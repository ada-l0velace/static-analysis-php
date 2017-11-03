class Identifier(Node):
    
    '''Class Identifier
          string kind
          string name
          string resolution'''
    
    def __init__(self, kind, name, resolution):
        super(kind)
        self.name = name 
        self.resolution = resolution
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name=name
        
    def getResolution(self):
        return self.resolution
    
    def setResolution(self, resolution):
        self.resolution = resolution
