# persistence layer for DataInterpreter CLI App
import csv


class DiPersistence(object):

    def load_csv(self, filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            try:
                return [row for row in reader if row]  # skip blank lines
            except csv.Error as e:
                raise csv.Error('file {}, line {}: {}'.format(filename, reader.line_num, e))from e
            except FileNotFoundError:
                raise
