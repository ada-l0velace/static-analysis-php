from Node import Node

class Entry(Node):
    
    '''
       Entry

       Extends Node

       An array entry - see Array

       Properties

           key (Node | null) The entry key/offset
           value Node The entry value
    '''
    
    def __init__(self, kind, key, value):
        super().__init__(kind)
        self.key = key
        self.value = value