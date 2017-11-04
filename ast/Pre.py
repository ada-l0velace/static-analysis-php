from Operation import Operation


class Pre(Operation):
    ''' Pre

        Extends Operation

        Defines a pre operation ++$i or --$i

        Properties

            type String
            what Variable
    '''

    def __init__(self, kind, type, what):
        super().__init__(kind)
        self.type = type
        self.what = what
