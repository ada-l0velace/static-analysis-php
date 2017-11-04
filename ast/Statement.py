from Node import Node


class Statement(Node):
    ''' Statement

        Extends Node

        Any statement.
    '''

    def __init__(self, kind):
        super().__init__(kind)