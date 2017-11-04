from Statement import Statement


class Retif(Statement):
    ''' RetIf

        Extends Statement

        Defines a short if statement that returns a value

        Properties

            test Expression
            trueExpr Expression
            falseExpr Expression
    '''

    def __init__(self, kind, test, trueExpr, falseExpr):
        super().__init__(kind)
        self.test = test
        self.trueExpr = trueExpr
        self.falseExpr = falseExpr
