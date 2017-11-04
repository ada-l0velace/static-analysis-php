from Statement import Statement


class Halt(Statement):
    ''' Halt

        Extends Statement

        Halts the compiler execution

        Properties

            after String String after the halt statement
    '''

    def __init__(self, kind, after):
        super().__init__(kind)
        self.after = after
