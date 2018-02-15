from index_exceptions import *
from bitarray import bitarray


class Index():

    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.indices = {}

    def add_index(self, condition):
        # This method creates bitarray with objects which apply
        # to the given condition
        #
        # Arguments:
        #   condition    A string with condition, which must be applied for the current data (e.g. "age > 5")

        bit_array = self.__add(condition)
        if bit_array is not None:
            self.indices[condition] = bit_array

    def __add(self, condition):
        try:
            field, op, value = self.__parse_condition(condition)
            if field not in self.data[0]:
                raise InvalidFieldName
            if "==" == op:
                return self.__equality(field, value)
            elif "<" != op:
                return self.__non_equality(field, value)
            elif ">=" == op:
                if(self.__is_number(value)):
                    return self.__great_or_equal(field, value)
                else:
                    raise InvalidValue
            elif ">" == op:
                if(self.__is_number(value)):
                    return self.__great(field, value)
                else:
                    raise InvalidValue
            elif "<=" == op:
                if(self.__is_number(value)):
                    return self.__less_or_equal(field, value)
                else:
                    raise InvalidValue
            elif "<" == op:
                if(self.__is_number(value)):
                    return self.__less_or_equal(field, value)
                else:
                    raise InvalidValue
            else:
                raise InvalidComparison
        except InvalidFieldName:
            print("Please, use correct field names.")
        except InvalidCondition:
            print("Please, use spaces in condition statements.")
        except InvalidComparison:
            print("Please, use correct comparison operator.")
        except InvalidValue:
            print("Please, use correct comparison for non-digit operators.")

    def __equality(self, field, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) == value:
                bits[i] = 1
        return bits

    def __non_equality(self, field, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) != value:
                bits[i] = 1
        return bits

    def __great_or_equal(self, field, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) >= value:
                bits[i] = 1
        return bits

    def __great(self, field, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) > value:
                bits[i] = 1
        return bits

    def __less_or_equal(self, field, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) <= value:
                bits[i] = 1
        return bits

    def __less(self, field, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) < value:
                bits[i] = 1
        return bits

    def __is_number(self, value):
        # Private method for checking if value is number or not
        #
        # Arguments:
        #   value    A string with/without number

        if value[0] in ('-', '+'):
            return value[1:].isdigit()
        return value.isdigit()

    def __parse_condition(self, condition):
        # Private method for parsing condition from a string to list of fieldname,
        # logical operation and value
        #
        # Arguments:
        #   condition    A string with condition, which must be applied for the current data (e.g. "age > 5")

        cond = condition.split(" ")
        if len(cond) == 3:
            return cond
        else:
            raise InvalidCondition

    def __get_by_id(self, ids):
        # Private method for getting necessary data by list of ids
        #
        # Arguments:
        #   ids    List with ids of elements
        pass

    def and_op(self, first_condition, second_condition):
        # This method applies bitwise operator 'and' to conditions
        # and returns list of objects which satisfy to conditions
        #
        # Arguments:
        #   first_condition    A string with condition (e.g. "age > 5")
        #   second_condition   A string with condition (e.g. "name == Ivan")

        try:
            if first_condition in self.indices:
                first_data = self.indices[first_condition]
            else:
                first_data = self.__add(first_condition)
                if first_data is None:
                    raise InvalidSearch
                self.indices[first_condition] = first_data
            if second_condition in self.indices:
                second_data = self.indices[second_condition]
            else:
                second_data = self.__add(second_condition)
                if second_data is None:
                    raise InvalidSearch
                self.indices[second_condition] = second_data
            result = first_data & second_data
            print(result)
            # TODO: return data
        except InvalidSearch:
            print("Problems with search. Check the exceptions above.")

    def or_op(self, first_condition, second_condition):
        # This method applies bitwise operator 'or' to conditions
        # and returns list of objects which satisfy conditions
        #
        # Arguments:
        #   first_condition    A string with condition (e.g. "age > 5")
        #   second_condition   A string with consdtion (e.g. "name == Ivan")

        try:
            if first_condition in self.indices:
                first_data = self.indices[first_condition]
            else:
                first_data = self.__add(first_condition)
                if first_data is None:
                    raise InvalidSearch
                self.indices[first_condition] = first_data
            if second_condition in self.indices:
                second_data = self.indices[second_condition]
            else:
                second_data = self.__add(second_condition)
                if second_data is None:
                    raise InvalidSearch
                self.indices[second_condition] = second_data
            result = first_data | second_data
            print(result)
            # TODO: return data
        except InvalidSearch:
            print("Problems with search. Check the exceptions above.")
