from Operation import Operation


class Unary(Operation):
    ''' Unary

        Extends Operation

        Unary operations

        Properties

            type String
            what Expression
    '''

    def __init__(self, kind, type, what):
        super().__init__(kind)
        self.type = type
        self.what = what
