import StringIO

class Pattern(object):
    """docstring for Pattern"""
    def __init__(self, name=None, inputs=None, sanitizations=None, sinks=None, patterns=None):
        super(Pattern, self).__init__()
        self.vars = {}
        self.id = None
        self.flows = {}
        if not patterns:
            self.name = name
            self.inputs = inputs
            self.sanitizations = sanitizations
            self.sinks = sinks
        else:
            self.parse_patterns(patterns)

    def is_sink(self, s):
        return s in self.sinks

    def is_sanitization(self, s):
        return s in self.sanitizations

    def is_input(self, i):
        return i in self.inputs

    def set_taintness(self, name, t):
        self.vars[name] = t

    def set_var_flow(self, var, flow):
        self.flows[var] = flow

    def get_var_flow(self, var):
        return self.flows.get(var, list())

    def get_var_taintness(self, name):
        return self.vars.get(name, False)

    def parse_patterns(self, pattern_string):
        buf = StringIO.StringIO(pattern_string)
        self.name = buf.readline().strip()
        for i in range(3):
            list_objects = buf.readline().strip().split(',')
            if i == 0:
                self.inputs = list_objects
            elif i == 1:
                self.sanitizations = list_objects
            elif i == 2:
                self.sinks = list_objects
            
class FlowItem(object):

    INPUT_TYPE = "Input"
    SANITIZATION_TYPE = "Sanitization"
    SINK_TYPE = "Sink"

    def __init__(self):
        self.line = -1
        self.name = ""
        self.type = ""

    def __repr__(self):
        return "{Flow Item line# %s name %s}" % (str(self.line), self.name)