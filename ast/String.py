from Literal import Literal


class String(Literal):
    ''' String

        Extends Literal

        Defines a nowdoc string

        Properties

            label String
    '''

    def __init__(self, kind, value, label):
        super().__init__(kind, value)
        self.label = label
