from Sys import Sys


class Unset(Sys):
    ''' Unset

        Extends Sys

        Deletes references to a list of variables
    '''
    def __init__(self, kind, arguments):
        super().__init__(kind, arguments)