from Statement import Statement


class Switch(Statement):
    ''' Switch

        Extends Statement

        Defines a switch statement

        Properties

            test Expression
            body Block
            shortForm boolean
    '''
    def __init__(self, kind, test, body, shortForm):
        super().__init__(kind)
        self.test = test
        self.body = body
        self.shortForm = shortForm