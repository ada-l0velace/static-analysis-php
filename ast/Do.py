from Statement import Statement


class Do(Statement):
    ''' Do

        Extends Statement

        Defines a do/while statement

        Properties

            test Expression
            body Statement
    '''

    def __init__(self, kind, test, body):
        super().__init__(kind)
        self.test = test
        self.body = body