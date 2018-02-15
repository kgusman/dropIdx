from Exceptions import *
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

        try:
            field, op, value = self.__parse_condition(condition)
            if "==" == op:
                self.indices[condition] = self.__equality(field, value)
            elif ">=" == op:
                if(self.__is_number(value)):
                    self.indices[condition] = self.__great_or_equal(
                        field, value)
                else:
                    raise InvalidValue
            elif ">" == op:
                if(self.__is_number(value)):
                    self.indices[condition] = self.__great(field, value)
                else:
                    raise InvalidValue
            elif "<=" == op:
                if(self.__is_number(value)):
                    self.indices[condition] = self.__less_or_equal(
                        field, value)
                else:
                    raise InvalidValue
            elif "<" == op:
                if(self.__is_number(value)):
                    self.indices[condition] = self.__less_or_equal(
                        field, value)
                else:
                    raise InvalidValue
            else:
                raise InvalidComparison
        except InvalidCondition:
            print("Please, use spaces in condition statements.")
        except InvalidComparison:
            print("Please, use correct comparison operator.")
        except InvalidValue:
            print("Please, use correct comparison for non-digit operators.")

    def __equality(self, field, value):
        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) == value:
                bits[i] = 1
        return bits

    def __great_or_equal(self, field, value):
        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) >= value:
                bits[i] = 1
        return bits

    def __great(self, field, value):
        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) > value:
                bits[i] = 1
        return bits

    def __less_or_equal(self, field, value):
        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) <= value:
                bits[i] = 1
        return bits

    def __less(self, field, value):
        bits = bitarray('0' * self.length)
        for i in range(self.length):
            if str(self.data[i][field]) < value:
                bits[i] = 1
        return bits

    def __is_number(self, value):
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
        pass

    def or_op(self, first_condition, second_condition):
        # This method applies bitwise operator 'or' to conditions
        # and returns list of objects which satisfy conditions
        #
        # Arguments:
        #   first_condition    A string with condition (e.g. "age > 5")
        #   second_condition   A string with consdtion (e.g. "name == Ivan")
        pass
