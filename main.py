#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from Tree import Tree

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = json.loads(open(sys.argv[1]).read())
    else:
        print 'Usage: python main.py samples/slice1.json'
        exit(0)

    def create_tree(treedict):
        return Tree(treedict)

    t = create_tree(data)
    #print str(t.root)
    calls = t.find_all_sinks(t.root, [])
    variables = []
    for i in calls:
        variables.append(i.arguments[0])

    assigns = t.find_all_kind('assign')
    current_var = variables[0]
    j = len(assigns)
    while current_var.kind != 'offsetlookup' or j < 0:
        for a in assigns[::-1]:
            if a.left.kind == 'variable':
                if hasattr(current_var, 'name'):
                    if a.left.name == current_var.name:
                        if a.right.kind == 'encapsed':
                            for b in a.right.values:
                                if b.kind == 'variable':
                                    current_var = b
                        elif a.right.kind == 'variable' or a.right.kind == 'offsetlookup':
                            current_var = a.right
                else:
                    if a.left.name == current_var.what.name:
                        if a.right.kind == 'encapsed':
                            for b in a.right.values:
                                if b.kind == 'variable':
                                    current_var = b
                        elif a.right.kind == 'variable' or a.right.kind == 'offsetlookup':
                            current_var = a.right
        j-=1
    if current_var.kind == 'offsetlookup':
        print 'SQL injection'
        print str(current_var).rstrip()
        print ','.join([x.what['name'] for x in calls])
