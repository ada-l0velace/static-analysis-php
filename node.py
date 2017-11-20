# Great Node Class
# class Node(object):
#     def __init__(self, json, parent = None):
#         self.parent = parent
#         for key in json:
#             if type(json[key]) == dict:
#                 self.__dict__[key] = Node(json[key], self)
#             elif type(json[key]) == list:
#                 self.__dict__[key] = []
#                 for i in json[key]:
#                     if type(i) == dict:
#                         self.__dict__[key] += [Node(i, self)]
#                     else:
#                         self.__dict__[key] += [i]
#             else:
#                 self.__dict__[key] = json[key]


class Node(object):
    def __init__(self, json, parent=None):
        self.parent = parent
        self.tainted = False
        self.flow_list = []
        self.line_start = json['loc']['start']['line'] - 2
        self.line_end = json['loc']['end']['line'] - 2
        for key in json:
            if type(json[key]) != dict:
                if type(json[key]) != list:
                    self.__dict__[key] = json[key]

    def is_infinite(self, node):
        return True


class IdentifierNode(Node):
    def __init__(self, json, parent=None):
        super(IdentifierNode, self).__init__(json, parent)


class ErrorNode(Node):
    def __init__(self, json, parent=None):
        super(ErrorNode, self).__init__(json, parent)


class BreakNode(Node):
    def __init__(self, json, parent=None):
        super(BreakNode, self).__init__(json, parent)
        if json["level"] != None:
            self.level = Number(json["level"], self)

    def is_infinite(self, node):
        return False
