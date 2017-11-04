from Statement import Statement


class Silent(Statement):
    ''' Silent

        Extends Statement

        Avoids to show/log warnings & notices from the inner expression

        Properties

            expr Expression
    '''
    def __init__(self, kind, expr):
        super().__init__(kind)
        self.expr = expr