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

    def validated(self, washed_list):
        """
        wash and validate data using re patterns
        if The input_list is valid return input_list else return None
        data that raises an exception returns None
        :return: Validated input_list or None
        """
        validated = None
        try:
            if re.fullmatch(self.RULES.get('id'), washed_list[0]) and \
               re.fullmatch(self.RULES.get('gender'), washed_list[1]) and \
               re.fullmatch(self.RULES.get('age'), washed_list[2]) and \
               re.fullmatch(self.RULES.get('sales'), washed_list[3]) and \
               re.fullmatch(self.RULES.get('bmi'), washed_list[4])and \
               re.fullmatch(self.RULES.get('income'), washed_list[5]):
                validated = washed_list
        except TypeError:
            pass
        except IndexError:
            pass
        finally:
            return validated
