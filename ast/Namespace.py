from Block import Block


class Namespace(Block):
    ''' Namespace

        Extends Block

        The main program node

        Properties

            name String
            withBrackets Boolean
    '''
    def __init__(self, kind, children, name, withBrackets):
        super().__init__(kind, children)
        self.name = name
        self.withBrackets = withBrackets