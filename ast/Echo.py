from Sys import Sys


class Echo(Sys):
    ''' Echo

        Extends Sys

        Defines system based call
    '''
    def __init__(self, kind, arguments):
        super().__init__(kind, arguments)