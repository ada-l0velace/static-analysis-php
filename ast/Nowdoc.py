from Literal import Literal


class Nowdoc(Literal):
    def __init__(self, kind, value):
        super().__init__(kind, value)