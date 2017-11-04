from Statement import Statement


class Clone(Statement):
    ''' Clone

        Extends Statement

        Defines a clone call

        Properties

        what Expression
    '''

    def __init__(self, kind, what):
        super().__init__(kind)
        self.what = what
