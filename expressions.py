class Exp(object):
	"""docstring for Exp"""
	def __init__(self, json=None):
		print json
		if json:
			self.json = json
			self.parse_from_json()

	def parse_from_json(self):
		for key in self.json:
			self.__dict__[key] = self.json[key]


class VariableExp(Exp):
	"""docstring for VariableExp"""
	def __init__(self, name=None, value=None, json={}):
		super(VariableExp, self).__init__(json)
		if json == {} and name !=None and value!= None:
			self.name = name
			self.value = value

class EntryPointsExp(Exp):
	"""docstring for EntryPointsExp"""
	def __init__(self, arg):
		super(EntryPointsExp, self).__init__()
		self.arg = arg
		

class BinaryOperatorExp(Exp):
	"""docstring for BinaryOperator"""
	def __init__(self, json):
		super(BinaryOperatorExp, self).__init__()
		self.operator = json['operator']
		self.left = VariableExp(json=json['left'])
		if json['right'] == 'offsetlookup':
			print json['right']['what']['name']
			#self.right = json['right']
		#print self.right
		#print self.left['name']#,self.right['kind']