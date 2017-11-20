class Operations(object):
    @staticmethod
    def operate(operator, left, right):
        o = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             '.': lambda x, y: x + y
             }
        return o[operator](left, right)

    @staticmethod
    def verify(operator, left, right):
        v = {'==': lambda x, y: x == y,
             '!=': lambda x, y: x != y,
             '>=': lambda x, y: x >= y,
             '<=': lambda x, y: x <= y,
             '<': lambda x, y: x < y,
             '>': lambda x, y: x > y
             }
        return v[operator](left, right)
