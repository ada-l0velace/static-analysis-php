from Statement import Statement


class ForEach(Statement):
    ''' Foreach

        Extends Statement

        Defines a foreach iterator

        Properties

            source Expression
            key (Expression | null)
            value Expression
            body Statement
            shortForm boolean
    '''
    def __init__(self,kind, source, key, value, body, shortForm):
        super().__init__(kind)
        self.source = source
        self.key = key
        self.value = value
        self.body = body
        self.shortForm = shortForm