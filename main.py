#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from Tree import Tree

from expressions import *
from fabric.fabric_all import *

def get_attrs(klass):
  return [k for k in klass.__dict__.keys()
            if not k.startswith('__')
            and not k.endswith('__')]

# Tree in JSON format
s = '{"kind":"program","loc":{"source":null,"start":{"line":1,"column":0,"offset":0},"end":{"line":6,"column":0,"offset":110}},"children":[{"kind":"assign","loc":{"source":null,"start":{"line":2,"column":0,"offset":6},"end":{"line":2,"column":22,"offset":28}},"operator":"=","left":{"kind":"variable","loc":{"source":null,"start":{"line":2,"column":0,"offset":6},"end":{"line":2,"column":2,"offset":8}},"name":"u","byref":false,"curly":false},"right":{"kind":"offsetlookup","loc":{"source":null,"start":{"line":2,"column":10,"offset":16},"end":{"line":2,"column":22,"offset":28}},"what":{"kind":"variable","loc":{"source":null,"start":{"line":2,"column":5,"offset":11},"end":{"line":2,"column":10,"offset":16}},"name":"_GET","byref":false,"curly":false},"offset":{"kind":"constref","loc":{"source":null,"start":{"line":2,"column":11,"offset":17},"end":{"line":2,"column":21,"offset":27}},"name":{"kind":"identifier","loc":{"source":null,"start":{"line":2,"column":11,"offset":17},"end":{"line":2,"column":21,"offset":27}},"resolution":"uqn","name":"‘username’"}}}},{"kind":"assign","loc":{"source":null,"start":{"line":3,"column":0,"offset":30},"end":{"line":3,"column":49,"offset":79}},"operator":"=","left":{"kind":"variable","loc":{"source":null,"start":{"line":3,"column":0,"offset":30},"end":{"line":3,"column":2,"offset":32}},"name":"q","byref":false,"curly":false},"right":{"kind":"bin","loc":{"source":null,"start":{"line":3,"column":43,"offset":73},"end":{"line":3,"column":49,"offset":79}},"type":".","left":{"kind":"bin","loc":{"source":null,"start":{"line":3,"column":5,"offset":35},"end":{"line":3,"column":49,"offset":79}},"type":".","left":{"kind":"string","loc":{"source":null,"start":{"line":3,"column":5,"offset":35},"end":{"line":3,"column":42,"offset":72}},"value":"SELECT pass FROM users WHERE user=’","isDoubleQuote":true},"right":{"kind":"variable","loc":{"source":null,"start":{"line":3,"column":43,"offset":73},"end":{"line":3,"column":45,"offset":75}},"name":"u","byref":false,"curly":false}},"right":{"kind":"string","loc":{"source":null,"start":{"line":3,"column":46,"offset":76},"end":{"line":3,"column":49,"offset":79}},"value":"’","isDoubleQuote":true}}},{"kind":"assign","loc":{"source":null,"start":{"line":4,"column":0,"offset":81},"end":{"line":4,"column":24,"offset":105}},"operator":"=","left":{"kind":"variable","loc":{"source":null,"start":{"line":4,"column":0,"offset":81},"end":{"line":4,"column":6,"offset":87}},"name":"query","byref":false,"curly":false},"right":{"kind":"call","loc":{"source":null,"start":{"line":4,"column":20,"offset":101},"end":{"line":4,"column":24,"offset":105}},"what":{"kind":"identifier","loc":{"source":null,"start":{"line":4,"column":9,"offset":90},"end":{"line":4,"column":20,"offset":101}},"resolution":"uqn","name":"mysql_query"},"arguments":[{"kind":"variable","loc":{"source":null,"start":{"line":4,"column":21,"offset":102},"end":{"line":4,"column":23,"offset":104}},"name":"q","byref":false,"curly":false}]}}],"errors":[]}'
# Convert JSON tree to a Python dict
data = json.loads(s)

literal = ['string', 'integer']
operations = ['bin', 'pre', 'post', 'parenthesis', 'unary', 'cast']
expressions = ['constref', 'variable', 'call'] + literal + operations
statements = ['assign', 'program']
nodes = ['identifier']
#print expressions
# Convert back to JSON & print to stderr so we can verfiy that the tree is correct.
#print(json.dumps(data, indent=4), file=sys.stderr)

# # Extract tree edges from the dict
# edges = []
# def get_edges(treedict, parent=None):
#     for i in treedict:
#         if i == 'kind' and treedict[i] == 'assign':
#             print BinaryOperatorExp(treedict)
#             #exit(0)
#         if  type(treedict[i]) == dict:
#             get_edges(treedict[i], i)
#         elif type(treedict[i]) == list:
#             for j in treedict[i]:
#                 get_edges(j, i)
# #get_edges(data)

#t = Tree(data)
#for i in t.root.children:
#    print i.value.__dict__()
# Extract tree edges from the dict
edges = []
def get_edges(treedict, parent=None):
    for i in treedict:
        if i == 'kind' and treedict[i] in expressions:
            a = FactoryProducer.get_factory(treedict[i], treedict, parent)
            #print get_attrs(a)
            print a.__dict__
            # if a.kind == 'bin':
            #     print a.left.__dict__
            #print BinaryOperatorExp(treedict)
            #exit(0)
        elif i == 'kind' and treedict[i] in statements:
            a = FactoryProducer.get_factory(treedict[i], treedict, parent)
            print a.__dict__
        elif i == 'kind' and treedict[i] in nodes:
            a = FactoryProducer.get_factory(treedict[i], treedict, parent)
            print a.__dict__
  
        if  type(treedict[i]) == dict:
            get_edges(treedict[i], i)
        elif type(treedict[i]) == list:
            for j in treedict[i]:
                get_edges(j, i)
#get_edges(data)

def create_tree(treedict):
  return Tree(treedict)

t = create_tree(data)


def transverse_tree(tree):
    print tree.__dict__
    if hasattr(tree, 'children'):
        for child in tree.children:
            transverse_tree(child)
    elif hasattr(tree, 'arguments'):
        for child in tree.arguments:
            transverse_tree(child)
    elif hasattr(tree, 'left') and hasattr(tree, 'right'): # binary
        transverse_tree(tree.left)
        transverse_tree(tree.right)
    elif hasattr(tree, 'left'): # unary left
        transverse_tree(tree.left)
    elif hasattr(tree, 'right'): # unary right
        transverse_tree(tree.right)
print str(t.root)
            
#transverse_tree(t.root)
