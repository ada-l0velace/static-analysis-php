from Constant import Constant


class ClassConstant(Constant):
    ''' ClassConstant

        Extends Constant

        Defines a class/interface/trait constant

        Properties

            isStatic boolean
            visibility string
    '''
    def __init__(self, kind, name, value, isStatic, visibility):
        super().__init__(kind, name, value)
        self.isStatic = isStatic
        self.visibility = visibility