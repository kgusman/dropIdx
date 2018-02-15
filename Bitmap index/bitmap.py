from index_exceptions import *
from bitarray import bitarray
from item import Item


class BitMap():

    def __init__(self, item_list, condition):
        self.data = item_list
        self.length = len(item_list)
        self.add_index(condition)

    def add_index(self, condition):
        # This method creates bitarray with objects which apply
        # to the given condition
        #
        # Arguments:
        #   condition    A string with condition, which must be applied for the current data (e.g. "age > 5")

        bit_array = self.__add(condition)
        if bit_array is not None:
            self.indices = bit_array.search(bitarray('1'))
            self.false_indices = bit_array.search(bitarray('0'))

    def search(self, item):
        # This method searches item in data
        #
        # Arguments:
        #   item    An item that has to be find
        
        if item.get_key() in self.indices:
            return item.get_key()
        elif item.get_key() in self.false_indices:
            return item.get_key()

    def __add(self, condition):
        try:
            op, value = self.__parse_condition(condition)
            if "==" == op:
                return self.__equality(value)
            elif "<" != op:
                return self.__non_equality(value)
            elif ">=" == op:
                if(self.__is_number(value)):
                    return self.__great_or_equal(value)
                else:
                    raise InvalidValue
            elif ">" == op:
                if(self.__is_number(value)):
                    return self.__great(value)
                else:
                    raise InvalidValue
            elif "<=" == op:
                if(self.__is_number(value)):
                    return self.__less_or_equal(value)
                else:
                    raise InvalidValue
            elif "<" == op:
                if(self.__is_number(value)):
                    return self.__less_or_equal(value)
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

    def __equality(self, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        bits.setall(False)
        for i, d in enumerate(self.data):
            if str(d.get_key()) == value:
                bits[i] = 1
        return bits

    def __non_equality(self, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        bits.setall(False)
        for i, d in enumerate(self.data):
            if str(d.get_key()) != value:
                bits[i] = 1
        return bits

    def __great_or_equal(self, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        bits.setall(False)
        for i, d in enumerate(self.data):
            if str(d.get_key()) >= value:
                bits[i] = 1
        return bits

    def __great(self, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        bits.setall(False)
        for i, d in enumerate(self.data):
            if str(d.get_key()) > value:
                bits[i] = 1
        return bits

    def __less_or_equal(self, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray('0' * self.length)
        bits.setall(False)
        for i, d in enumerate(self.data):
            if str(d.get_key()) <= value:
                bits[i] = 1
        return bits

    def __less(self, value):
        # This private method returns bitarray with 1's where the whole condition satisfies
        #
        # Arguments:
        #   field    A string with name of field
        #   value    A string with value

        bits = bitarray(self.length)
        bits.setall(False)
        for i, d in enumerate(self.data):
            if str(d.get_key()) < value:
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
        if len(cond) == 2:
            return cond
        else:
            raise InvalidCondition

    def __get_by_id(self, ids):
        # Private method for getting found data
        #
        # Arguments:
        #   ids    List with ids of elements
        result = []
        for ind in ids:
            result.append(self.data[ind])
        return result

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
            return self.__get_by_id(result.search(bitarray('1')))
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
            return self.__get_by_id(result.search(bitarray('1')))
        except InvalidSearch:
            print("Problems with search. Check the exceptions above.")
