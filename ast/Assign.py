from Statement import Statement


class Assign(Statement):
    ''' Assign

        Extends Statement

        Assigns a value to the specified target

        Properties

            left Expression
            right Expression
            operator String
    '''

    def __init__(self, kind, left, right, operator):
        super().__init__(kind)
        self.left = left
        self.right = right
        self.operator = operator