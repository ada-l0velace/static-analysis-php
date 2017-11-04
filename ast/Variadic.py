from Expression import Expression


class Variadic(Expression):
    ''' Variadic

        Extends Expression

        Introduce a list of items into the arguments of the call

        Properties

            what (Array | Expression)
    '''
    def __init__(self, kind, what):
        super().__init__(kind)
        self.what = what