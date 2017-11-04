from Sys import Sys


class Isset(Sys):
    ''' Isset

        Extends Sys

        Defines an isset call
    '''
    def __init__(self, kind, arguments):
        super().__init__(kind, arguments)