from Expression import Expression


class Lookup(Expression):
    ''' Lookup

        Extends Expression

        Lookup on an offset in the specified object

        Properties

            what Expression
            offset Expression
    '''
    def __init__(self, kind, what, offset):
        super().__init__(kind)
        self.what = what
        self.offset = offset