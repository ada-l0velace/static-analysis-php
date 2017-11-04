from Statement import Statement


class Exit(Statement):
    ''' Exit

        Extends Statement

        Defines an exit / die call

        Properties

            status (Node | null)
    '''

    def __init__(self, kind, status):
        super().__init__(kind)
        self.status = status
