from Operation import Operation


class Parenthesis(Operation):
    ''' Parenthesis

        Extends Operation

        Parenthesis encapsulation (... expr ...)

        Properties

            inner Expression
    '''

    def __init__(self, kind, inner):
        super().__init__(kind)
        self.inner = inner
