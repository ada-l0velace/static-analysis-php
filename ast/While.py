from Statement import Statement


class While(Statement):
    ''' While

        Extends Statement

        Defines a while statement

        Properties

            test Expression
            body Statement
            shortForm boolean
    '''

    def __init__(self, kind, test, body, shortForm):
        super().__init__(kind)
        self.test = test
        self.body = body
        self.shortForm = shortForm
