from Declaration import Declaration


class Trait(Declaration):
    ''' Trait

        Extends Declaration

        A trait definition

        Properties

            extends (Identifier | null)
            implements Array<Identifier>
            body Array<Declaration>
    '''
    def __init__(self, kind, name, extends, implements, body):
        super().__init__(kind, name)
        self.extends = extends
        self.implements = implements
        self.body = body