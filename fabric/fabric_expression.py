import sys
import os
import expressions

class ExpressionFactoryProducer(object):
    @staticmethod
    def get_factory(kind, json,parent):
        d = {'variable': expressions.VariableExp,
             'constref': expressions.ConsrefExp,
             'bin': expressions.BinaryOperatorExp,
             'string': expressions.StringExp,
             'offsetlookup': expressions.OffsetlookupExp,
             'call' : expressions.CallExp,
             'encapsed' : expressions.EncapsedExp,
             'number' : expressions.NumberExp}
        return d[kind](json=json,parent=parent)
