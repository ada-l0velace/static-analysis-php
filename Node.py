class Node(object):
    def __init__(self, json, parent = None):
        self.parent = parent
        for key in json:
            if type(json[key]) == dict:
                self.__dict__[key] = Node(json[key], self)
            elif type(json[key]) == list:
                self.__dict__[key] = []
                for i in json[key]:
                    if type(i) == dict:
                        self.__dict__[key] += [Node(i, self)]
                    else:
                        self.__dict__[key] += [i]
            else:
                self.__dict__[key] = json[key]
