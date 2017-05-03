"""
This object is function as the loader for the user input file,
it should find the user-friendly input file(csv) and load the
information from the file.

Below is the description:
path: where is the list of employee information
set_path: find out if there is a path directed to the csv file,
    if yes, check if it is correct.
    if not, set it up

"""


class FileLoader:

    def __init__(self):
        self.path = ''

    def set_path(self):
        result = 'n'
        while result != 'y':
            if self.path != '':
                print("Is this the correct path:{} y/n"
                      .format(self.path))
                result = input()
                if result != 'y':
                    self.path = ''
                else:
                    self.path = input("Please enter the full address of the file --> ")

    def file_loader(self):
        pass




