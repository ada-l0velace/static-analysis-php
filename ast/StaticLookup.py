from Lookup import Lookup


class StaticLookup(Lookup):
    ''' StaticLookup

        Extends Lookup

        Lookup to a static property
    '''
    def __init__(self, kind, what, offset):
        super().__init__(kind,what,offset)