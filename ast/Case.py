from Node import Node

class Case(Node):
    
    ''' Case

        Extends Node

        A switch case statement

        Properties
  
           test (Expression | null) if null, means that the default case
           body (Block | null)
    '''
    
    def __init__(self, kind, test, body):
        super().__init__(kind)
        self.test = test
        self.body = body