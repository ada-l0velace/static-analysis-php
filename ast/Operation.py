from Expression import Expression


class Operation(Expression):
    ''' Operation

        Extends Expression

        Defines binary operations
    '''
    def __init__(self, kind):
        super().__init__(kind)