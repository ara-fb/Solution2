import re


class FieldValidator:
    """wash and validate asingle field"""
    def __init__(self, name, rule):
        self.__name = name
        self.__rule = rule

    def wash(self, field_str):
        return field_str.strip().capitalize()

    def validate(self, field_str):
        return re.fullmatch(self.__rule, field_str)

    def __str__(self):
        return self.__name + " validator\nRule: " + self.__rule


class Validator:
    """
    wash and validate data for a  single record
    """
    def __init__(self):
        self.__fields = []
        self.__add_all_fields()

    def __add_all_fields(self):
        self.__fields.append(FieldValidator('id', '[A-Z][0-9]{3}'))
        self.__fields.append(FieldValidator('gender', '(M|F)'))
        self.__fields.append(FieldValidator('age', '[0-9]{2}'))
        self.__fields.append(FieldValidator('sales', '[0-9]{3}'))
        self.__fields.append(FieldValidator('bmi', '(Normal|Overweight|Obesity|Underweight)'))
        self.__fields.append(FieldValidator('income', '[0-9]{2,3}'))


    def wash(self, input_list):
        """return washed  data"""
        washed = []
        try:
            for field, data in zip(self.__fields, input_list):
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
        :return: is_valid , validated
        """
        result = False, None
        try:
            for field, data in zip(self.__fields, washed_list):
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
