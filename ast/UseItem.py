from Statement import Statement


class UseItem(Statement):
    ''' UseItem

        Extends Statement

        Defines a use statement (from namespace)

        Properties

            name String
            type (String | null) Possible value : function, const
            alias (String | null)
    '''
    def __init__(self, kind, name, type, alias):
        super().__init__(kind)
        self.name = name
        self.type = type
        self.alias = alias