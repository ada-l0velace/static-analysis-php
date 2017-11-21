from node import Node
from fabric.fabric_all import *
import inspect
from operations import Operations


class Exp(Node):
    """docstring for Exp"""

    def __init__(self, json=None, parent=None):
        super(Exp, self).__init__(json, parent)


class ConsrefExp(Exp):
    """docstring for ConsrefExp"""

    def __init__(self, json, parent):
        super(ConsrefExp, self).__init__(json, parent)


class OffsetlookupExp(Exp):
    """docstring for OffsetlookupExp"""

    def __init__(self, json, parent):
        super(OffsetlookupExp, self).__init__(json, parent)

        self.name = json['what']['name']
        self.offset = json['offset']['value']

    def get_value(self):
        return self.name

        #self.name = self.what['name']

    def __repr__(self):
        return repr('$' + self.name) + '[' + repr(self.offset) + ']'


class VariableExp(Exp):
    """docstring for VariableExp"""

    def __init__(self, json, parent):
        super(VariableExp, self).__init__(json, parent)
        # print json
        self.name = json["name"]
        self.value = ""

    def __repr__(self):
        return '$' + self.name

    def get_value(self):
        return self.value


class EncapsedExp(Exp):
    """docstring for EncapsedExp"""

    def __init__(self, json, parent):
        super(EncapsedExp, self).__init__(json, parent)
        self.values = []
        # print json
        for a in json["value"]:
            self.values += [FactoryProducer.get_factory(a['kind'], a, self)]

    def get_value(self):
        value = ""
        for i in self.values:
            value += i.get_value()
        return value

    def __repr__(self):
        return ''.join([x.__str__() for x in self.values])


class CallExp(Exp):
    def __init__(self, json, parent):
        super(CallExp, self).__init__(json, parent)
        self.arguments = []
        self.name = json['what']['name']
        #self.name = self.what['name']
        for a in json["arguments"]:
            self.arguments += [FactoryProducer.get_factory(a['kind'], a, self)]

    def get_value(self):
        return self.name

    def __repr__(self):
        return self.name + '(' + ','.join([x.__str__() for x in self.arguments]) + ')'

# OPERATORS


class BinaryOperatorExp(Exp):
    """docstring for BinaryOperator"""

    def __init__(self, json, parent):
        super(BinaryOperatorExp, self).__init__(json, parent)

        self.left = FactoryProducer.get_factory(
            json["left"]["kind"], json["left"], self)
        self.right = FactoryProducer.get_factory(
            json["right"]["kind"], json["right"], self)

    def get_value(self):
        return Operations.operate(self.type, self.left.get_value(), self.right.get_value())

    def __repr__(self):
        return self.left.__str__() + self.type + self.right.__str__()

    def is_valid(self):
        return Operations.verify(self.type, self.left.get_value(), self.right.get_value())


class PostOperatorExp(Exp):
    """docstring for BinaryOperator"""

    def __init__(self, json, parent):
        super(PostOperatorExp, self).__init__(json, parent)
        self.what = FactoryProducer.get_factory(
            json["what"]["kind"], json["what"], self)

    def get_value(self):
        return Operations.operate(self.type, self.what.get_value(), 1)

    def __repr__(self):
        return str(self.what) + self.type * 2

    def is_infinite(self, node):
        if self.what.name == node.name:
            return False
        return True


class ParenthesisOperatorExp(Exp):
    """docstring for BinaryOperator"""

    def __init__(self, json, parent):
        super(ParenthesisOperatorExp, self).__init__(json, parent)
        self.name = self.kind
        self.inner = FactoryProducer.get_factory(
            json['inner']['kind'], json['inner'], self)

    def get_value(self):
        return self.inner.get_value()

    def __repr__(self):
        return '(' + self.inner.__str__() + ')'


# LITERALS

class StringExp(Exp):
    """docstring for StringExp"""

    def __init__(self, json, parent):
        super(StringExp, self).__init__(json, parent)

    def __repr__(self):
        return '"' + self.value + '"'

    def get_value(self):
        return self.value


class NumberExp(Exp):
    """docstring for NumberExp"""

    def __init__(self, json, parent):
        super(NumberExp, self).__init__(json, parent)

    def is_valid(self):
        if self.value == 0:
            return False
        return True

    def get_value(self):
        return int(self.value)

    def __repr__(self):
        return str(self.value)


class BooleanExp(Exp):
    """docstring for BooleanExp"""

    def __init__(self, json, parent):
        super(BooleanExp, self).__init__(json, parent)

    def is_valid(self):
        return not self.get_value()

    def get_value(self):
        return bool(self.value)

    def __repr__(self):
        return str(self.value).lower()
