import sys
import os
import node

class NodeFactoryProducer(object):
    @staticmethod
    def get_factory(kind, json, parent):
        d = { 'identifier' : node.IdentifierNode}
        return d[kind](json, parent)
