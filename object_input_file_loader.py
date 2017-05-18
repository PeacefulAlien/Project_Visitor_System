"""
This object is function as the loader for the user input file.
input file MUST be csv format to avoid confusion and be user friendly
there are also functions can be used to redirect the working directory,
file name and validate the file.

Below is the description for each function:
set_file_path:
    validate the working directory
    change if necessary

set_file_name:
    validate the input file name and format
    change if necessary

file_validation:
    some simple step check for data validation and integration
    before load into database

file_loader: load the information in the user-friendly excel file
    and save the data to local database for further usage.
"""


import os
import csv
import objcet_database_main


class FileLoader(objcet_database_main.DatabaseMain):

    def __init__(self):
        super().__init__()
        self.file_path = 'C:\\Users\\sunzao\\Documents\\Python\\Project_Visitor_System\\input'
        self.file_name = 'employee_input_list.csv'

    def set_file_path(self):
        option_01 = 'n'
        while option_01 != 'y':
            print("Is the input file in this path?\n{}\ny/n ".format(self.file_path))
            option_01 = str(input())
            if option_01 == 'y':
                print("Current working path is\n -->{}".format(os.getcwd()))
                break
            else:
                self.file_path = str(input("Please enter the full path to the input file\n--> "))
                os.chdir(self.file_path)

    def set_file_name(self):
        option_03 = 'n'
        while option_03 != 'y':
            print("Is this the right input file name?\n{}\ny/n ".format(self.file_name))
            option_03 = str(input())
            if option_03 == 'y':
                print("Current input file name is\n --> {}".format(self.file_name))
                break
            else:
                self.file_name = str(input("Please enter the name of the input file\n--> "))

    def file_validation(self):
        if os.path.isfile(os.path.join(self.file_path, self.file_name)):
            with open(os.path.join(self.file_path, self.file_name)) as raw:

                # checkout header
                header = csv.Sniffer().has_header(raw.read(1024))
                if not header:
                    raise ValueError("The file has no header. Please check the input file!")
                # else:
                #     print(header)
                raw.seek(0)

                # checkout dialect
                dialect = csv.Sniffer().sniff(raw.read(1024))
                # print(dialect.delimiter)
                raw.seek(0)

                # checkout data
                data = []
                reader = csv.reader(raw, dialect)
                next(raw)
                for row in reader:
                    data.append(row)
                if not data:
                    raise ValueError("There is no content in the file! Please check the input file!")
        else:
            raise ValueError('The required file does not exist at the location!')

    def file_loader(self):
        self.basic_info_table_reset()
        with open(os.path.join(self.file_path, self.file_name)) as raw:
            dialect = csv.Sniffer().sniff(raw.read(1024))
            raw.seek(0)
            reader = csv.reader(raw, delimiter=dialect.delimiter)
            next(reader, None)
            for field in reader:
                self.basic_info_table_data_entry(field)





















