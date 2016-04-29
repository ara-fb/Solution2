# DataInterpreter - facade for the Model
import re
from csv import Error as csvErr


class DataInterpreter:
    """
    Interpret data loaded in from a file
    load data from a file and validate.
    extract data by type
    """
    RECORD_COLUMNS = ['id', 'gender', 'age', 'sales', 'bmi', 'income']

    def __init__(self, persistence, validator):
        self.__valid_records = []
        self.__validator = validator
        self.__persistence = persistence
        self.__load_status = ""

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
        count_invalid = 0
        count_valid = 0
        invalid_data_ids = []
        status = []
        for data_list in all_data:
            is_valid, validated = self.__validated(data_list)
            if is_valid:
                self.__valid_records.append(validated)
                count_valid += 1
            else:
                invalid_data_ids.append(data_list[0])
                count_invalid += 1
        status.append(str(count_valid) + ' records added')
        if count_invalid:
            status.append(str(count_invalid) + ' invalid records skipped')
            status.append('Invalid data at id = ' + ' '.join(invalid_data_ids))
        self.__load_status = '\n'.join(status)

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
        assert data_name in self.RECORD_COLUMNS
        data_array = []
        for data in self.__valid_records:
            item = data[self.RECORD_COLUMNS.index(data_name)]
            data_array.append(item)
        return data_array

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
        return self.__valid_records
