from Statement import Statement


class Throw(Statement):
    ''' Throw

        Extends Statement

        Defines a throw statement

        Properties

            what Expression
    '''
    def __init__(self, kind, what):
        super().__init__(kind)
        self.what = what