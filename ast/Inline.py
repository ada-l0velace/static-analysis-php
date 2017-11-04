from Literal import Literal


class Inline(Literal):
    ''' Inline

        Extends Literal

        Defines inline html output (treated as echo output)
    '''

    def __init__(self, kind, value):
        super().__init__(kind, value)
