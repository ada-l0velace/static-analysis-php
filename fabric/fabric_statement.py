import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import statements 

class StatementFactoryProducer(object):
    @staticmethod
    def get_factory(kind, json, parent):
        d = { 'assign' : statements.AssignStm,
              'program' : statements.ProgramStm}
        return d[kind](json, parent)
