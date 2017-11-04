from Literal import Literal


class Encapsed(Literal):
    ''' Encapsed

        Extends Literal

        Defines an encapsed string (contains expressions)

        Properties

            type String Defines the type of encapsed string (shell, heredoc, string)
            label (String | Null) The heredoc label, defined only when the type is heredoc
    '''

    def __init__(self, kind, value, type, label):
        super().__init__(kind, value)
        self.type = type
        self.label = label
