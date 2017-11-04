from Statement import Statement


class Declare(Statement):
    ''' Declare

        Extends Block

        The declare construct is used to set execution directives for a block of code

        Properties

            what Array<Expression>
            mode String
    '''

    def __init__(self, kind, what, mode):
        super().__init__(kind)
        self.what = what
        self.mode = mode
