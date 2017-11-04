from Declaration import Declaration


class Parameters(Declaration):
    ''' Parameter

        Extends Declaration

        Defines a function parameter

        Properties

            type (Identifier | null)
            value (Node | null)
            byref boolean
            variadic boolean
            nullable boolean
    '''
    def __init__(self, kind, name, type, value, byref, variadic, nullable):
        super().__init__(kind, name)
        self.type = type
        self.value = value
        self.byref = byref
        self.variadic = variadic
        self.nullable = nullable