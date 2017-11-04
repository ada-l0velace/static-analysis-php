from Statement import Statement


class Try(Statement):
    ''' Try

        Extends Statement

        Defines a try statement

        Properties

            body Block
            catches Array<Catch>
            allways Block
    '''
    def __init__(self, kind, body, catches, allways):
        super().__init__(kind)
        self.body = body
        self.catches = catches
        self.allways = allways