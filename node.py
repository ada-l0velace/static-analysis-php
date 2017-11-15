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
        for key in json:
            if type(json[key]) != dict:
                if type(json[key]) != list:
                    self.__dict__[key] = json[key]

    def __str__(self, level=0):
        ret = "\t"*level+repr(self)+"\n"
        if hasattr(self, 'children'):
            for child in self.children:
                ret += child.__str__(level+1)
        elif hasattr(self, 'left') and hasattr(self, 'right'):
            ret += self.left.__str__(level+1)
            ret += self.right.__str__(level+1)
        elif hasattr(self, 'arguments'):
            for arg in self.arguments:
                ret += arg.__str__(level+1)
        elif hasattr(self, 'values'):
            for val in self.values:
                ret += val.__str__(level+1)
        elif hasattr(self, 'body'):

            ret += self.test.__str__(level+1)
            for val in self.body.children:
                ret += val.__str__(level+1)
            if hasattr(self, 'alternate') and self.alternate != None:
                ret += self.alternate.__str__(level+1)
            

        return ret

class IdentifierNode(Node):
    def __init__(self, json, parent=None):
        super(IdentifierNode, self).__init__(json, parent)
