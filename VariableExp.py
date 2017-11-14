class VariableExp(Exp):
	"""docstring for VariableExp"""
	def __init__(self, name=None, value=None, json={}):
		super(VariableExp, self).__init__()
		if json == {} and name !=None and value!= None:
			self.name = name
			self.value = value
		