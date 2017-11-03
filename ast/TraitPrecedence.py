from Node import Node

class TraitPrecedence(Node):
    
    '''
       TraitPrecedence

       Extends Node

       Defines a trait alias

       Properties

          trait (Identifier | null)
          method string
          instead Array<Identifier>
    '''
    
    def __init__(self, kind, trait, method, instead):
        super().__init__(kind)
        self.trait = trait
        self.method = method
        self.instead = instead