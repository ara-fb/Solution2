from csv import Error as csvErr
from collections import OrderedDict


class Record:
    __RULES = [('id', '[A-Z][0-9]{3}'),
               ('gender', '(M|F)'),
               ('age', '[0-9]{2}'),
               ('sales', '[0-9]{3}'),
               ('bmi', '(Normal|Overweight|Obesity|Underweight)'),
               ('income', '[0-9]{2,3}')]

    def __init__(self, the_id, gender, age, sales, bmi, income):
        self.field_values = OrderedDict()
        self.field_values['id'] = the_id
        self.field_values['gender'] = gender
        self.field_values['age'] = age
        self.field_values['sales'] = sales
        self.field_values['bmi'] = bmi
        self.field_values['income'] = income

    def get_by_name(self, data_name):
        assert data_name in self.field_values
        return self.field_values.get(data_name)

    def get_all_as_array(self):
        return list(self.field_values.values())

    @classmethod
    def get_rules(cls):
        return cls.__RULES

    @classmethod
    def get_bmi_options(cls):
        return ['Normal', 'Overweight', 'Obesity', 'Underweight']


class DataInterpreter:
    """
    Interpret data loaded in from a file
    load data from a file and validate.
    extract data by type
    """

    def __init__(self, persistence, validator):
        self.__valid_records = []
        self.__validator = validator
        self.__persistence = persistence
        self.__load_status = ""
        # Give the rules to the validator
        rules = Record.get_rules()
        self.__validator.add_all_fields(rules)

    def load_csv(self, file_path):
        """
        use persistence object to get data at [file_path]
        pass data to add function
        :param file_path: string file_path
        :return: None
        """
        try:
            self.__add_data(self.__persistence.load_csv(file_path))
        except FileNotFoundError:
            self.__load_status = "No file found at " + file_path + ". Please enter a valid file path."
        except csvErr:  # not sure this is the best way to catch the csv Error?
            self.__load_status = "csv_err"

    def __add_data(self, all_data):
        """
        add valid data
        generate message about invalid data
        :param all_data: list containing data for multiple records
        """
        count_valid = 0
        invalid_data_ids = []
        status = ''
        for data_list in all_data:
            is_valid, validated_data = self.__validated(data_list)
            if is_valid:
                self.__add_validated_record(validated_data)
                count_valid += 1
            else:
                invalid_data_ids.append(data_list[0])
        status += str(count_valid) + ' records added'
        if invalid_data_ids:
            status += self.__invalid_data_message(invalid_data_ids)
        self.__load_status = status

    def __add_validated_record(self, valid_data):
        the_id, gender, age, sales, bmi, income = valid_data[0], valid_data[1], valid_data[2],\
                                                      valid_data[3], valid_data[4], valid_data[5]
        record = Record(the_id, gender, age, sales, bmi, income)
        self.__valid_records.append(record)

    def __invalid_data_message(self, invalid_data_ids):
        invalid_count = str(len(invalid_data_ids))
        invalid_mesg = '\n' + invalid_count + ' invalid records skipped\n'
        invalid_mesg += 'Invalid data at id = ' + ' '.join(invalid_data_ids)
        return invalid_mesg

    def __validated(self, input_list):
        """
        wash and validate data using Validator object
        :return: is_valid, validated_list
        """
        washed_list = self.__validator.wash(input_list)
        return self.__validator.validated(washed_list)

    def get_load_status(self):
        """
        get the load status
        :return: load status
        """
        return self.__load_status

    def get_valid_data(self, data_name):
        """
        extract data by type
        :param data_name: name of the data
        :return: data_array of valid [data_name] values
        """
        return [record.get_by_name(data_name) for record in self.__valid_records]

    def get_bmi_distribution(self):
        bmi_counts = [0,0,0,0]
        for record in self.__valid_records:
            bmi = record.field_values['bmi']
            if bmi == "Normal":
                bmi_counts[0] += 1
            elif bmi == "Overweight":
                bmi_counts[1] +=1
            elif bmi == "Obesity":
                bmi_counts[2] +=1
            elif bmi == "Underweight":
                bmi_counts[3] +=1
        return bmi_counts

    def get_bmi_options(self):
        return Record.get_bmi_options()

    def contains_valid_records(self):
        """
        return true if there are valid records, otherwise return false
        :return: True or False
        """
        if self.__valid_records:
            return True
        return False

    # for testing purposes
    def get_all_valid_records(self):
        """only for testsing - return all record data as arrays"""
        return [record.get_all_as_array() for record in self.__valid_records]

    def count_valid_data(self):
        return len(self.__valid_records)
