from Statement import Statement


class Eval(Statement):
    ''' Eval

        Extends Statement

        Defines an eval statement

        Properties

            source Node
    '''

    def __init__(self, kind, source):
        super().__init__(kind)
        self.source = source
