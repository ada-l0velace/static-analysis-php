from Statement import Statement


class New(Statement):
    ''' New
        Extends Statement

        Creates a new instance of the specified class

        Properties

        what (Identifier | Variable | Class)
        arguments Array<Arguments>
    '''
    def __init__(self, kind, what, arguments):
        super().__init__(kind)
        self.what = what
        self.arguments = arguments