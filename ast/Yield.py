from Expression import Expression


class Yield(Expression):
    ''' Yield

        Extends Expression

        Defines a yield generator statement

        Properties

            value (Expression | Null)
            key (Expression | Null)
    '''
    def __init__(self, kind, value, key):
        super().__init__(kind)
        self.value = value
        self.key = key