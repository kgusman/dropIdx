class InvalidCondition(Exception):
	""" Raised when the input cond """
	pass

class InvalidComparison(Exception):
	""" Raised when the input contains invalid comparison operator"""
	pass

class InvalidValue(Exception):
	""" Raised when the value is invalid """
	pass

class InvalidSearch(Exception):
	""" Raised if there some problems with search """
	pass