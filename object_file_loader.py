"""
This object is function as the loader for the user input file,
it should find the user-friendly input file(csv) and load the
information from the file.

Below is the description:
path: where is the list of employee information
set_path: find out if there is a path directed to the csv file,
    if yes, check if it is correct.
    if not, set it up

file_loader: load the information in the user-friendly excel file
    and save the information for further usage.

set_size: the information from input file can be edited from time to time
    to be able to change the storage, this method added flexibility to the
    data storage.

"""


import os
import csv
import objcet_employee_basic_info


class FileLoader(objcet_employee_basic_info.EmployeeBasicInfo):

    def __init__(self):
        super().__init__()
        self.path = ''
        # self.width = 10
        # self.height = 10
        self.input_list = {}

    def set_path(self):
        option_01 = 'n'
        while option_01 != 'y':
            self.path = os.getcwd()
            print("Is the input file in this path?\n{}\ny/n ".format(self.path))
            option_01 = str(input())
            if option_01 == 'y':
                print("Current working path is\n -->{}".format(os.getcwd()))
                break
            else:
                self.path = str(input("Please enter the full path to the input file\n--> "))
                os.chdir(self.path)

    # def set_size(self):
    #     option_02 = input("Do you want to change the size of the input list? y/n ")
    #     if option_02 == 'y':
    #         self.width = input("How many cells do you want in each row --> ")
    #         self.height = input("How many rows do you want in the input list --> ")
    #     print("Current input list Size: {} by {}".format(self.width, self.height))

    def file_loader(self):
        self.path = 'C:\\Users\sunzao\Documents\Python\Project_Visitor_System\input'
        os.chdir(self.path)
        with open('employee_input_list.csv') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            print(header)
        with open('employee_input_list.csv') as csvfile:
            self.input_list = csv.DictReader(csvfile)
            for row in self.input_list:
                print(row)





















