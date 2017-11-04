from Statement import Statement


class Catch(Statement):
    ''' Catch

        Extends Statement

        Defines a catch statement

        Properties

            what Array<Identifier>
            variable Variable
            body Statement
    '''
    def __init__(self, kind, what, variable, body):
        super().__init__(kind)
        self.what = what
        self.variable = variable
        self.body = body