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

    def validated(self, input_list):
        """
        wash and validate data using re patterns
        if The input_list is valid return input_list else return None
        data that raises an exception returns None
        :return: Validated input_list or None
        """
        validated = None
        washed = []
        try:
            for in_str in input_list:
                washed.append(str(in_str.strip()))
            # fix case on alphabetic characters
            washed[0] = washed[0].upper()
            washed[1] = washed[1].upper()
            washed[4] = washed[4].capitalize()
            if re.fullmatch(self.RULES.get('id'), washed[0]) and \
               re.fullmatch(self.RULES.get('gender'), washed[1]) and \
               re.fullmatch(self.RULES.get('age'), washed[2]) and \
               re.fullmatch(self.RULES.get('sales'), washed[3]) and \
               re.fullmatch(self.RULES.get('bmi'), washed[4])and \
               re.fullmatch(self.RULES.get('income'), washed[5]):
                validated = washed
        except TypeError:
            pass
        except IndexError:
            pass
        finally:
            return validated
