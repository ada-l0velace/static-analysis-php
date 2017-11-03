from Node import Node

class TraitUse(Node):
    
    ''' Extends Node

        Defines a trait usage

        Properties

           traits Array<Identifier>
           adaptations (Array<Node> | null)
    '''
    
    def __init__(self, kind, traits, adaptations):
        super().__init__(kind)
        self.traits = traits
        self.adaptations = adaptations
        
    def getTraits(self):
        return self.traits
    
    def setTraits(self, traits):
        self.traits = traits
        
    def getAdaptations(self):
        return self.adaptations
    
    def setAdaptations(self, adaptations):
        self.adaptations = adaptations