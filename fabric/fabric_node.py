import sys
import os
import node


class NodeFactoryProducer(object):
    @staticmethod
    def get_factory(kind, json, parent):
        d = {'identifier': node.IdentifierNode,
             'error': node.ErrorNode,
             'break': node.BreakNode
             }
        return d[kind](json, parent)
