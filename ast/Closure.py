from Statement import Statement


class Closure(Statement):
    ''' Closure

        Extends Statement

        Defines a closure

        Properties

            arguments Array<Parameter>
            uses Array<Variable>
            type Identifier
            byref boolean
            nullable boolean
            body (Block | null)
            isStatic boolean
    '''
    def __init__(self, kind, arguments, uses, type, byref, nullable, body, isStatic):
        super().__init__(kind)
        self.arguments = arguments
        self.uses = uses
        self.type = type
        self.byref = byref
        self.nullable = nullable
        self.body = body
        self.isStatic = isStatic