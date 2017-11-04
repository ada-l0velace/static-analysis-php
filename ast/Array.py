from Expression import Expression


class Array(Expression):
    ''' Array

        Extends Expression

        Defines an array structure

        Properties

            items Array<Entry> List of array items
            shortForm boolean Indicate if the short array syntax is used, ex [] instead array()
    '''
    def __init__(self, kind, items, shortForm):
        super().__init__(kind)
        self.items = items
        self.shortForm = shortForm