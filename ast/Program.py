from Block import Block


class Program(Block):
    ''' Program

        Extends Block

        The main program node

        Properties

            errors Array<Error>
    '''
    def __init__(self, kind, children, errors):
        super().__init__(kind,children)
        self.errors = errors