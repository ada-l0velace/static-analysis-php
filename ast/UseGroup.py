from Statement import Statement


class UseGroup(Statement):
    ''' UseGroup

        Extends Statement

        Defines a use statement (with a list of use items)

        Properties

            name (String | null)
            type (String | null) Possible value : function, const
            item Array<UseItem>
    '''
    def __init__(self, kind, name, type, item):
        super().__init__(kind)
        self.name = name
        self.type = type
        self.item = item