from Node import Node


class Expression(Node):
    ''' Expression

        Extends Node

        Any expression node. Since the left-hand side of an assignment may be any expression in general, an expression can also be a pattern.
    '''
    
    def __init__(self, kind):
        super().__init__(kind)