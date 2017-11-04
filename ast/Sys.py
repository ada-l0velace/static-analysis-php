from Statement import Statement


class Sys(Statement):
    '''Sys

        Extends Statement

        Defines system based call

        Properties

            arguments Array<Node>
    '''
    def __init__(self, kind, arguments):
        super().__init__(kind)
        self.arguments = arguments