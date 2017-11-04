from Lookup import Lookup


class OffsetLookup(Lookup):
    ''' OffsetLookup

        Extends Lookup

        Lookup on an offset in an array
    '''
    def __init__(self, kind, what, offset):
        super().__init__(kind, what, offset)