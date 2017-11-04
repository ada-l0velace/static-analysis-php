from Statement import Statement


class For(Statement):
    ''' For

        Extends Statement

        Defines a for iterator

        Properties

            init Array<Expression>
            test Array<Expression>
            increment Array<Expression>
            body Statement
            shortForm boolean
    '''

    def __init__(self, kind, init, test, increment, body, shortForm):
        super().__init__(kind)
        self.init = init
        self.test = test
        self.increment = increment
        self.body = body
        self.shortForm = shortForm