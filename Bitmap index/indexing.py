class Index():

	def __init__(data):
		self.data = data

	def add_index(condition):
	# This method creates bitarray with objects which apply
	# to the given condition
	#
	# Arguments:
	#	condition    A string with condition, which must be applied for the current data (e.g. "age > 5")
	pass

	def __parse_condition(condition):
		# Private method for parsing condition from a string to list of fieldname,
		# logical operation and value
		#
		# Arguments:
		#	condition    A string with condition, which must be applied for the current data (e.g. "age > 5")
		pass

	def __get_by_id(ids):
		# Private method for getting necessary data by list of ids
		#
		# Arguments:
		#	ids    List with ids of elements 
		pass

	def and_op(first_condition, second_condition):
		# This method applies bitwise operator 'and' to conditions
		# and returns list of objects which satisfy to conditions
		#
		# Arguments:
		#	first_condition    A string with condition (e.g. "age > 5")
		#	second_condition   A string with condition (e.g. "name == Ivan")
		pass

	def or_op(first_condition, second_condition):
		# This method applies bitwise operator 'or' to conditions
		# and returns list of objects which satisfy conditions
		#
		# Arguments:
		#	first_condition    A string with condition (e.g. "age > 5")
		#	second_condition   A string with consdtion (e.g. "name == Ivan")
		pass
