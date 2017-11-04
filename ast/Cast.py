from Operation import Operation


class Cast(Operation):
    ''' Extends Operation

        Binary operations

        Properties

            type String
            what Expression
    '''

    def __init__(self, kind, type, what):
        super().__init__(kind)
        self.type = type
        self.what = what