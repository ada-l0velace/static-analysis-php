from Expression import Expression


class YieldForm(Expression):
    ''' YieldFrom

        Extends Expression

        Defines a yield from generator statement

        Properties

            value Expression
    '''
    def __init__(self, kind, value):
        super().__init__(kind)
        self.value = value