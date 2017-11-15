import sys
import os
from fabric_statement import StatementFactoryProducer
from fabric_expression import ExpressionFactoryProducer
from fabric_node import NodeFactoryProducer

class FactoryProducer(object):
    @staticmethod
    def get_factory(kind, json, parent):
        literal = ['string', 'integer']
        operations = ['bin', 'pre', 'post', 'parenthesis', 'unary', 'cast']
        expressions = ['constref', 'variable', 'call', 'offsetlookup'] + literal + operations
        statements = ['assign', 'program']
        nodes = ['identifier']
        if kind in expressions:
            return ExpressionFactoryProducer.get_factory(kind, json, parent)
        elif kind in statements:
            return StatementFactoryProducer.get_factory(kind, json, parent)
        elif kind in nodes:
            return NodeFactoryProducer.get_factory(kind, json, parent)
   