from Declaration import Declaration


class Interface(Declaration):
    ''' Interface

        Extends Declaration

        An interface definition

        Properties

            extends Array<Identifier>
            body Array<Declaration>
    '''
    def __init__(self, kind, name, extends, body):
        super().__init__(kind, name)
        self.extends = extends
        self.body = body