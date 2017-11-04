from Statement import Statement


class Block(Statement):
    ''' Block

        Extends Statement

        A block statement, i.e., a sequence of statements surrounded by braces.

        Properties

            children Array<Node>
    '''
    def __init__(self, kind, children):
        super().__init__(kind)
        super.children = children