from Statement import Statement


class Goto(Statement):
    ''' Goto

        Extends Statement

        Defines goto statement

        Properties

            label String
    '''
    def __init__(self, kind, label):
        super().__init__(kind)
        self.label = label