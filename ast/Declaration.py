from Statement import Statement


class Declaration(Statement):
    ''' Declaration

        Extends Statement

        A declaration statement (function, class, interface...)

        Properties

            name string
    '''

    def __init__(self, kind, name):
        super().__init__(kind)
        self.name = name
