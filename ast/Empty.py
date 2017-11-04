from Sys import Sys


class Empty(Sys):
    ''' Empty

        Extends Sys

        Defines an empty check call
    '''
    def __init__(self, kind, arguments):
        super().__init__(kind, arguments)