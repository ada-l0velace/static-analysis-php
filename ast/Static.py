from Statement import Statement


class Static(Statement):
    ''' Static

        Extends Statement

        Declares a static variable into the current scope

        Properties

            items (Array<Variable> | Array<Assign>)
    '''

    def __init__(self, kind, items):
        super().__init__(kind)
        self.items = items
