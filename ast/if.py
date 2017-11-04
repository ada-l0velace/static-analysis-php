from Statement import Statement


class If(Statement):
    ''' If

        Extends Statement

        Defines a if statement

        Properties

            test Expression
            body Block
            alternate (Block | If | null)
            shortForm boolean
    '''

    def __init__(self, kind, test, body, alternate, shortForm):
        super().__init__(kind)
        self.test = test
        self.body = body
        self.alternate = alternate
        self.shortForm = shortForm