#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from Tree import Tree
from pattern import *
import StringIO

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = json.loads(open(sys.argv[1]).read())
    else:
        print 'Usage: python main.py samples/slice1.json'
        exit(0)

    def create_tree(treedict):
        return Tree(treedict)

    t = create_tree(data)
    patterns = ''
    with open('patterns/patts', 'r') as f:
        patterns = f.read()
    
    #print patterns
    pattern = ''
    patts = StringIO.StringIO(patterns)
    for i in range(1,len(patterns.split('\n'))+1):
        pattern += patts.readline()
        if i % 4 == 0:
            t.visit(t.root, Pattern(patterns=pattern))
            pattern = ''
            patts.readline()
    #print str(t.root)
    
