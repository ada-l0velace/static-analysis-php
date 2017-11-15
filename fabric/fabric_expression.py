import sys
import os
import expressions

class ExpressionFactoryProducer(object):
    @staticmethod
    def get_factory(kind, json):
        d = {'variable': expressions.VariableExp,
             'constref': expressions.ConsrefExp,
             'bin': expressions.BinaryOperatorExp,
             'string': expressions.StringExp,
             'offsetlookup': expressions.OffsetlookupExp}
        return d[kind](json=json)
