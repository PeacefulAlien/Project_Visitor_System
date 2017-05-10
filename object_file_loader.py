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


class FileLoader:

    def __init__(self):
        self.path = ''
        self.width = 10
        self.height = 10
        self.input_list = {}
        self.header = []

    def set_path(self):
        option_01 = 'n'
        while option_01 != 'y':
            if self.path != '':
                print("Is this the correct path?\n{}\ny/n".format(self.path))
                option_01 = input()
                if option_01 == 'y':
                    break
                else:
                    self.path = ''
            else:
                self.path = input("Please enter the full path to the file --> ")

    def set_size(self):
        option_02 = input("Do you want to change the size of the input list? y/n ")
        if option_02 == 'y':
            self.width = input("How many cells do you want in each row --> ")
            self.height = input("How many rows do you want in the input list --> ")
        print("Current input list Size: {} by {}".format(self.width, self.height))

    def file_loader(self):
        os.chdir('C:\\Users\sunzao\Documents\Python\Project_Visitor_System\input')
        with open('employee_input_list.csv') as csvfile:
            self.input_list = csv.DictReader(csvfile)
            self.header = self.input_list.fieldnames
            for key in self.header:
                print(self.input_list(key))












