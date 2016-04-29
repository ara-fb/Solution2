import re

class FieldValidator:
    def __init__(self, name, rule, input_order):
        self.__name = name
        self.__rule = rule
        self.__input_order = input_order

    def wash(self, field_str):
        return field_str.strip().capitalize()

    def validate(self, field_str):
        return re.fullmatch(self.__rule, field_str)

class Validator:
    """
    wash and validate data for a  single record
    """
    def __init__(self):
        self.fields = []
        self.__add_all_fields()

    def __add_all_fields(self):
        self.fields.append(FieldValidator('id', '[A-Z][0-9]{3}', 0))
        self.fields.append(FieldValidator('gender', '(M|F)', 1))
        self.fields.append(FieldValidator('age', '[0-9]{2}', 2))
        self.fields.append(FieldValidator('sales', '[0-9]{3}', 3))
        self.fields.append(FieldValidator('bmi', '(Normal|Overweight|Obesity|Underweight)', 4))
        self.fields.append(FieldValidator('income', '[0-9]{2,3}', 5))


    def wash(self, input_list):
        """return washed  data"""
        washed = []
        try:
            for field, data in zip(self.fields, input_list):
                washed.append(field.wash(data))
        except TypeError:
            raise
        except IndexError:
            raise
        finally:
            return washed

    def validated(self, washed_list):
        """
        wash and validate data using re patterns
        if The input_list is valid return input_list else return None
        data that raises an exception returns None
        :return: is_valid , validated
        """
        result = False, None
        try:
            for field, data in zip(self.fields, washed_list):
                if not field.validate(data):
                    break
            else:
                result = True, washed_list
        except TypeError:
             pass
        except IndexError:
             pass
        finally:
            return result
