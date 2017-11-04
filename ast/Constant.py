from Declaration import Declaration


class Constant(Declaration):
    ''' Constant

        Extends Declaration

        Defines a namespace constant

        Properties

            value (Node | null)
    '''
    def __init__(self, kind, name, value):
        super().__init__(kind, name)
        self.value = value