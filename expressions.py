from fabric.fabric_expression import *

class Exp(object):
	"""docstring for Exp"""
	def __init__(self, json=None):	
		self.parse_from_json(json)

	def parse_from_json(self, json):
		literal = ['string', 'integer']
		operations = ['bin', 'pre', 'post', 'parenthesis', 'unary', 'cast']
		expressions = ['constref', 'variable'] + literal + operations
		for key in json:
			if type(json[key]) == dict and json[key].has_key('kind') and json[key]['kind'] in expressions:
				self.__dict__[key] = ExpressionFactoryProducer.get_factory(json[key]['kind'], json[key])
			else:	
				if key not in ['loc', 'byref', 'curly', 'resolution']:
					self.__dict__[key] = json[key]


class ConsrefExp(Exp):
	"""docstring for ConsrefExp"""
	def __init__(self, json={}):
		super(ConsrefExp, self).__init__(json)

class OffsetlookupExp(Exp):
	"""docstring for OffsetlookupExp"""
	def __init__(self, json={}):
		super(OffsetlookupExp, self).__init__(json)
		
class VariableExp(Exp):
	"""docstring for VariableExp"""
	def __init__(self, name=None, value=None, json={}):
		super(VariableExp, self).__init__(json)

class EntryPointsExp(Exp):
	"""docstring for EntryPointsExp"""
	def __init__(self, arg):
		super(EntryPointsExp, self).__init__()
		self.arg = arg

#### OPERATORS
		
class BinaryOperatorExp(Exp):
	"""docstring for BinaryOperator"""
	def __init__(self, json):
		super(BinaryOperatorExp, self).__init__(json)

#### LITERALS

class StringExp(Exp):
	"""docstring for StringExp"""
	def __init__(self, json):
		super(StringExp, self).__init__(json)

