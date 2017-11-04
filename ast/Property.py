from Declaration import Declaration


class Property(Declaration):
    ''' Property

        Extends Declaration

        Defines a class property

        Properties

            isFinal boolean
            isStatic boolean
            visibility string
            value (Node | null)
    '''
    def __init__(self, kind, name, isFinal, isStatic, visibility, value):
        super().__init__(kind, name)
        self.isFinal = isFinal
        self.isStatic = isStatic
        self.visibility = visibility
        self.value = value
