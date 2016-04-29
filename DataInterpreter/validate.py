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

    def __validate_id(self,id_str):
        return re.fullmatch(self.RULES.get('id'), id_str)

    def __validate_gender(self, gender_str):
        return re.fullmatch(self.RULES.get('gender'), gender_str)

    def __validate_age(self, age_str):
        return re.fullmatch(self.RULES.get('age'), age_str)

    def __validate_sales(self, sales_str):
        return re.fullmatch(self.RULES.get('sales'), sales_str)

    def __validate_bmi(self, bmi_str):
        return re.fullmatch(self.RULES.get('bmi'), bmi_str)

    def __validate_income(self, income_str):
        return re.fullmatch(self.RULES.get('income'), income_str)


    def validated(self, washed_list):
        """
        wash and validate data using re patterns
        if The input_list is valid return input_list else return None
        data that raises an exception returns None
        :return: Validated input_list or None
        """
        validated = None
        try:
            if self.__validate_id( washed_list[0]) and \
               self.__validate_gender( washed_list[1]) and \
               self.__validate_age( washed_list[2]) and \
               self.__validate_sales( washed_list[3]) and \
               self.__validate_bmi( washed_list[4])and \
               self.__validate_income( washed_list[5]):
                validated = washed_list
        except TypeError:
            pass
        except IndexError:
            pass
        finally:
            return validated
