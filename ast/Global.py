from Statement import Statement


class Global(Statement):
    ''' Global

        Extends Statement

        Imports a variable from the global scope

        Properties

            items Array<Variable>
    '''

    def __init__(self, kind, items):
        super().__init__(kind)
        self.items = items
