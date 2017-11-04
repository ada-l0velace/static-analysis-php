from Declaration import Declaration


class Function(Declaration):
    ''' Function

        Extends Declaration

        Defines a classic function

        Properties

            arguments Array<Parameter>
            type Identifier
            byref boolean
            nullable boolean
            body (Block | null)
    '''
    def __init__(self, kind, name, arguments, type, byref, nullable, body):
        super().__init__(kind, name)
        self.arguments = arguments
        self.type = type
        self.byref = byref
        self.nullable = nullable
        self.body = body