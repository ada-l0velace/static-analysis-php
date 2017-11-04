from Expression import Expression


class ConstRef(Expression):
    ''' ConstRef

        Extends Expression

        A constant reference

        Properties

            name (String | Node)
    '''
    def __init__(self, kind, name):
        super().__init__(kind)
        self.name = name