import re


class Validator:
    """
    wash and validate data
    """
    RULES = {'id': '[A-Z][0-9]{3}',
             'gender': '(M|F)',
             'age': '[0-9]{2}',
             'sales': '[0-9]{3}',
             'bmi': '(Normal|Overweight|Obesity|Underweight)',
             'income': '[0-9]{2,3}'}

    def __wash_field(self, field_str):
        return field_str.strip().capitalize()

    def wash(self, input_list):
        """return washed  data"""
        washed = []
        try:
            for in_str in input_list:
                washed.append(in_str.strip().capitalize())
        except TypeError:
            raise
        except IndexError:
            raise
        finally:
            return washed

    def __validate_field(self, field_name, field_str):
        return re.fullmatch(self.RULES.get(field_name), field_str)


    def validated(self, washed_list):
        """
        wash and validate data using re patterns
        if The input_list is valid return input_list else return None
        data that raises an exception returns None
        :return: is_valid , validated
        """
        input_order = ['id','gender','age', 'sales','bmi','income']
        try:
            for index in range(6):
                if not self.__validate_field(input_order[index], washed_list[index]):
                    result = False, None
                    break
            else:
                result = True, washed_list
        except TypeError:
             result = False, None
        except IndexError:
             result = False, None
        finally:
            return result
