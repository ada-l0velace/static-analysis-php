from Literal import Literal


class Boolean(Literal):
    ''' Boolean

        Extends Literal

        Defines a boolean value (true/false)
    '''

    def __init__(self, kind, value):
        super().__init__(kind, value)