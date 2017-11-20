import StringIO

class bcolors:
    OKBLUE = '\033[44m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    WHITE = '\033[37m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Pattern(object):
    """docstring for Pattern"""
    def __init__(self, name=None, inputs=None, sanitizations=None, sinks=None, patterns=None):
        super(Pattern, self).__init__()
        self.vars = {}
        self.values = {}
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

    def set_value(self, name, v):
        self.values[name] = v

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

def flow_has_inputs(flow_list):
    for item in flow_list:
        if item.type == FlowItem.INPUT_TYPE:
            return True
    return False

def print_flow_list(flow_list, parsed_lines):
    def get_line_key(item):
        return item.line

    def select_types(l, type):
        for item in l:
            if item.type == type:
                format_string = "{%s %s}"
                if item.type == FlowItem.INPUT_TYPE:
                    format_string = bcolors.WHITE + bcolors.RED + format_string + bcolors.ENDC
                elif item.type == FlowItem.SANITIZATION_TYPE:
                    format_string = bcolors.WHITE + bcolors.GREEN + format_string + bcolors.ENDC
                else:
                    format_string = bcolors.OKBLUE + format_string + bcolors.ENDC
                format_string += "\n    %s"
                print format_string % (item.type, item.name, parsed_lines[item.line-2])

    if not flow_has_inputs(flow_list):
        return
    sorted_flow_list = sorted(flow_list, key=get_line_key)
    print "****************************** START FLOW  *****************************************"
    select_types(sorted_flow_list, FlowItem.INPUT_TYPE)
    select_types(sorted_flow_list, FlowItem.SANITIZATION_TYPE)
    select_types(sorted_flow_list, FlowItem.SINK_TYPE)
    print "******************************* END FLOW  ******************************************"         

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
