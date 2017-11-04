from Literal import Literal


class Number(Literal):
    ''' Number

        Extends Literal

        Defines a numeric value
    '''

    def __init__(self, kind, value):
        super().__init__(kind, value)
