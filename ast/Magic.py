from Literal import Literal


class Magic(Literal):
    ''' Magic

        Extends Literal

        Defines magic constant
    '''

    def __init__(self, kind, value):
        super().__init__(kind, value)
