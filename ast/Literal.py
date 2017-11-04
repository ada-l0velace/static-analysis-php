from Expression import Expression


class Literal(Expression):
    ''' Literal

        Extends Expression

        Defines an array structure

        Properties

            value (Node | string | number | boolean | null)
    '''

    def __init__(self, kind, value):
        super().__init__(kind)
        self.value = value
