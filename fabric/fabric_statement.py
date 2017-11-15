import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import statements 

class StatementFactoryProducer(object):
    @staticmethod
    def get_factory(kind, json, parent):
        d = { 'assign' : statements.AssignStm,
              'program' : statements.ProgramStm,
              'sys' : statements.SysStm,
              'echo' : statements.EchoStm,
              'if' : statements.IfStm,
              'while' : statements.WhileStm,
              'block' : statements.BlockStm
        }
        return d[kind](json, parent)
