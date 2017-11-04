from Function import Function


class Method(Function):
    ''' Method

        Extends Function

        Defines a class/interface/trait method

        Properties

            isAbstract boolean
            isFinal boolean
            isStatic boolean
            visibility string
    '''
    def __init__(self, kind, name, arguments, type, byref, nullable, body, isAbstract, isFinal, isStatic, visibility):
        super().__init__(kind, name, arguments, type, byref, nullable, body)
        self.isAbstract = isAbstract
        self.isFinal = isFinal
        self.isStatic = isStatic
        self.visibility = visibility
