import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import expressions

class ExpressionFactoryProducer(object):
    @staticmethod
    def get_factory(kind, json):
        d = {'variable': expressions.VariableExp,
             'constref': expressions.ConsrefExp,
             'bin': expressions.BinaryOperatorExp,
             'string': expressions.StringExp}
        return d[kind](json=json)