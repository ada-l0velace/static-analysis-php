from Operation import Operation


class Bin(Operation):
    ''' Bin

        Extends Operation

        Binary operations

        Properties

            type String
            left Expression
            right Expression
    '''

    def __init__(self, kind, type, left, right):
        super().__init__(kind)
        self.type = type
        self.left = left
        self.right = right
