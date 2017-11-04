from Declaration import Declaration


class Class(Declaration):
    ''' Class

        Extends Declaration

        A class definition

        Properties

            extends (Identifier | null)
            implements Array<Identifier>
            body Array<Declaration>
            isAnonymous boolean
            isAbstract boolean
            isFinal boolean
    '''
    def __init__(self, kind, name, extends, implements, body, isAnonymous, isAbstract, isFinal):
        super().__init__(kind, name)
        self.extends = extends
        self.implements = implements
        self.body = body
        self.isAnonymous = isAnonymous
        self.isAbstract = isAbstract
        self.isFinal = isFinal