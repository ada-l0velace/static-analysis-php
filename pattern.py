class Pattern(object):
    """docstring for Pattern"""
    def __init__(self, name, inputs, sanitizations, sinks):
        super(Pattern, self).__init__()
        self.vars = {}
        self.id = None
        self.name = name
        self.inputs = inputs
        self.sanitizations = sanitizations
        self.sinks = sinks
        self.flows = {}
    
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
        return self.vars.get(name, True)


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