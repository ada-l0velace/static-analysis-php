#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from Tree import Tree

from expressions import *
from fabric.fabric_all import *

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = json.loads(open(sys.argv[1]).read())
    else:
        print 'Usage: python main.py samples/slice1.json'
        exit(0)

    def create_tree(treedict):
      return Tree(treedict)

    t = create_tree(data)
    print str(t.root)