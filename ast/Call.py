from Statement import Statement


class Call(Statement):
    ''' Call

        Extends Statement

        Executes a call statement

        Properties

            arguments Array<Arguments>
    '''
    def __init__(self, kind, arguments):
        super().__init__(kind)
        self.arguments = arguments