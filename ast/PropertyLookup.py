from Lookup import Lookup


class PropertyLookup(Lookup):
    ''' Extends Lookup

        Lookup to an object property
    '''
    def __init__(self, kind, what, offset):
        super().__init__(kind,what,offset)