from Statement import Statement


class Include(Statement):
    ''' Include

        Extends Statement

        Defines system include call

        Properties

            target Node
            once boolean
            require boolean
    '''

    def __init__(self, kind, target, once, require):
        super().__init__(kind)
        self.target = target
        self.once = once
        self.require = require
