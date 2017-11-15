#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from Tree import Tree
from pattern import *

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = json.loads(open(sys.argv[1]).read())
    else:
        print 'Usage: python main.py samples/slice1.json'
        exit(0)

    def create_tree(treedict):
        return Tree(treedict)

    t = create_tree(data)
    t.visit(t.root, Pattern('SQL injection', 
        ['_GET','_POST','_COOKIE'], 
        ['mysql_escape_string','mysql_real_escape_string','mysql_real_escape_string'],
        ['mysql_query','mysql_unbuffered_query','mysql_db_query']))
    #print str(t.root)
    
