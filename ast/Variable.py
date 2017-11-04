from Expression import Expression


class Variable(Expression):
    ''' Variable

        Extends Expression

        Any expression node. Since the left-hand side of an assignment may be any expression in general, an expression can also be a pattern.

        Properties

            name (String | Node) The variable name (can be a complex expression when the name is resolved dynamically)
            byref boolean Indicate if the variable reference is used, ex &$foo
            curly boolean Indicate if the name is defined between curlies, ex ${foo}
    '''
    def __init__(self, kind, name, byref, curly):
        super().__init__(kind)
        self.name = name
        self.byref = byref
        self.curly = curly