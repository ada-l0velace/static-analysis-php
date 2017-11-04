from Operation import Operation


class Post(Operation):
    ''' Post

        Extends Operation

        Defines a post operation $i++ or $i--

        Properties

            type String
            what Variable
    '''

    def __init__(self, kind, type, what):
        super().__init__(kind)
        self.type = type
        self.what = what
