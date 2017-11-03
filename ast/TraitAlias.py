from Node import Node

class TraitAlias(Node):
    
    ''' TraitAlias

        Extends Node

        Defines a trait alias

        Properties
       
           trait (Identifier | null)
           method string
           aas (string | null)
           visibility (string | null)
    '''
    
    def __init__(self, kind, trait, method, aas, visibility):
        super().__init__(kind)
        self.trait = trait
        self.method = method
        self.aas = aas
        self.visibility = visibility
        